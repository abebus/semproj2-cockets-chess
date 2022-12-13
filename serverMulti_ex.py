import datetime
import socket
from time import sleep

from threading import Thread
from multiprocessing import Process, Manager, Lock
from typing import List

from queue import Queue
import pickle

class Lobby(Process):
	def __init__(self, index, shared_clients_list):
		"""
		Args:
			index:
			server_socket (socket.socket):
			shared_clients_list:
		"""
		super().__init__()
		self.lock = Lock()
		self.index = index
		self.clients: List[socket.socket] = shared_clients_list

	@staticmethod
	def parse_from_client(binary):
		data = pickle.loads(binary)
		msg = data.get('text')
		from_name = data.get('from')
		date = data.get('when')
		return msg, from_name, date

	@staticmethod
	def form_answer(text, data):
		packet = {"server": 'kek',
		          "text": text,
		          "data": data}
		binary = pickle.dumps(packet)
		return binary

	def worker(self):
		while True:
			data = self.q.get()
			print('get task from queue')
			self.send_all(data)
			self.q.task_done()

	def recv_client(self, sock):
		while 1:
			# get from client
			packet = sock.recv(1024)
			msg, from_name, date = self.parse_from_client(packet)

			# form answer
			out_data = self.form_answer(text=f"[{from_name}][{date}]::{msg}", data=None)

			# send to queue for broadcasting
			self.q.put(out_data)


	def add_client(self, client_socket, ip, port):
		print("client added to the lobby")
		self.clients.append(client_socket)

		self.lock.release()

		print("a new thread for client is created")

	@staticmethod
	def send(sock, binary_data):
		sock.send(binary_data)

	def send_all(self, binary_data):
		print('get task from queue')
		for client_socket in self.clients:
			client_socket.send(binary_data)

	def run(self):
		clients_threads = []

		self.q = Queue()
		self.queue_workers = [Thread(target=self.worker) for _ in range(5)]
		for w in self.queue_workers:
			w.start()

		while 1:
			self.lock.acquire()

			with self.lock:
				# add client to another Thread
				new_client = self.clients[-1]
				thread = Thread(target=self.recv_client, args=(new_client,))
				thread.start()
				clients_threads.append(thread)

				binary_data = self.form_answer(text=f"вы в лобби [{self.index}]", data=None)
				self.send(new_client, binary_data)

			# check if number of users is enough for starting the game
			# todo add

		# not reachable
		for w in self.workers:
			w.terminate()
			w.join()

class Server:
	def __init__(self, address):
		self.manager = Manager()

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# re-open port if busy
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind(address)
		self.sock.listen(4 * 10)
		self.clients = set()
		self.history = []

		self.lobbies_num = 4
		self.shared_clients_lists = [self.manager.list() for _ in range(self.lobbies_num)]

		self.lobbies = []
		for index, shared_clients in enumerate(self.shared_clients_lists):
			lobby = Lobby(index, shared_clients)
			self.lobbies.append(lobby)

		for lobby in self.lobbies:
			lobby.start()

	def remove_client(self, client):
		pass # ????

	def start_server(self):
		# FIXME ONLY FOR DEMONSTRATION!!!!

		to_which_lobby = iter([0, 0, 1, 0, 1])
		print("Server started")

		while 1:
			print("Waiting client...")
			client_socket, (ip, port) = self.sock.accept()
			print(f"Client ip={ip} [{port}] connected")

			print(f"A new client {ip} {port}")
			index = next(to_which_lobby)
			print(f"adding cleint to the lobby {index}")
			self.lobbies[index].add_client(client_socket, ip, port)

		# not reachable
		for lobby in self.lobbies:
			lobby.join()

address = ("127.0.0.1", 10000)
server = Server(address)
server.start_server()