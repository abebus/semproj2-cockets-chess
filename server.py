import socket
from time import sleep

from threading import Thread

import pickle
from protocol import Protocol, asdict


class ConnectedClient(Thread):
    def __init__(self, server, client_socket, ip, port):
        super().__init__()
        self.sock = client_socket
        self.server = server
        self.ip = ip
        self.port = port

    def run(self):
        while 1:
            print('yeeeeeeeeeeeeeeeeeeeeee')
            info = self.recv()
            msg = info.get('text')
            from_name = info.get('author')
            text = f"[{from_name}]::{msg}"
            self.server.send(text)

    def send(self, text):
        # protocol = {"text": text,
        #             "from": self.name}
        protocol = Protocol(text, self.name)
        protocol = asdict(protocol)
        print('protocol', protocol)
        self.sock.send(pickle.dumps(protocol))

    def recv(self):
        print('get')
        obj = self.sock.recv(1024)
        info = pickle.loads(obj)
        return info


class Server:
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # re-open port if busy
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.listen(2)
        self.clients = set()

    def send(self, text):
        for client in self.clients:
            client.send(text)

    def start_server(self):
        while 1:
            print('yeyeyeyeeyyeye')
            print(self)
            client_socket, (ip, port) = self.sock.accept()
            print(f"Client ip={ip} [{port}] connected")
            connected_client = ConnectedClient(self, client_socket, ip, port)
            connected_client.start()
            self.clients.add(connected_client)
            # welcome msg because argment list is empty


address = ("127.0.0.1", 10000)
server = Server(address)
server.start_server()
