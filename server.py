import socket
from time import sleep

from threading import Thread

import pickle
from protocol import Protocol, asdict
from main import BackendClient


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
            print(info)
            match info.data_type:
                case 'message':
                    self.server.send(info.text)
                case 'emoji':
                    ...
                case 'coords':
                    self.server.send(info.from_pos)

    send = BackendClient.send

    # def send(self, data_type, **kwargs):
    #     # protocol = {"text": text,
    #     #             "from": self.name}
    #     match data_type:
    #         case 'message':
    #             protocol = Protocol(data_type=data_type, author=self.name, text=kwargs['text'])
    #         case 'emoji':
    #             protocol = Protocol(data_type=data_type, author=self.name, emoji=kwargs['emoji'])
    #         case 'coords':
    #             protocol = Protocol(data_type=data_type, author=self.name,
    #                                 from_pos=kwargs['from_pos'],
    #                                 to_pos=kwargs['to_pos'])  # цвет не надо уточнять, это сделается на стороне
    #                                                                # сервера, будет проверка ход валидный ваще нет,
    #                                                                # пусть клиент передаёт всё что захочет
    #         case _:
    #             protocol = None
    #             print(kwargs)
    #             print('!!!no protocol, empty or unimplemented button pressed ')
    #
    #     #protocol = asdict(protocol)
    #     print('protocol', protocol)
    #     if protocol is not None:
    #         self.sock.send(pickle.dumps(protocol))

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
            print(client)
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
