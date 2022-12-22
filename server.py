import random
import socket
from time import sleep

from threading import Thread

import pickle


class ConnectedClient(Thread):
    def __init__(self, server, client_socket, ip, port, color, name):
        super().__init__()
        self.sock = client_socket
        self.server = server
        self.ip = ip
        self.port = port
        self.color = color
        self.name = name

    def run(self):
        while 1:
            info = self.recv()
            if len(info) == 1:
                msg = info.get('text')
                name = self.name
                text = f"[{name}]::{msg}"
                self.server.send(text)
            elif len(info) == 2:
                y = info.get('y')
                x = info.get('x')
                color = self.color
                self.server.send(y, x, color)
            elif len(info) == 3:
                text = info.get('text')
                a = ''
                self.server.send(text, a)
            elif len(info) == 5:
                a = info.get('a')
                b = info.get('b')
                y = info.get('y')
                x = info.get('x')
                txt = info.get('txt')
                color = self.color
                print('informasion',self.color, self.name)
                self.server.send(a, b, y, x, txt, color)

    def send(self, *args):
        print('send', len(args), args, '\n\n')
        if len(args) == 1:
            protocol = {"text": args[0]}
            self.sock.send(pickle.dumps(protocol))
        elif len(args) == 2:
            protocol = {"text": args[0], "": ""}
            self.sock.send(pickle.dumps(protocol))
        elif len(args) == 3:
            protocol = {"y": args[0], "x": args[1],
                        "color": args[2]}
            self.sock.send(pickle.dumps(protocol))
        elif len(args) == 6:
            protocol = {"a": args[0], "b": args[1],
                        "y": args[2], "x": args[3],
                        "txt": args[4], "color": args[5]}
            self.sock.send(pickle.dumps(protocol))

    def recv(self):
        obj = self.sock.recv(1024)
        info = pickle.loads(obj)
        print('recv-info:', info)
        return info


class Server:
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # re-open port if busy
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.listen(2)
        self.clients = set()
        self.colors = set()

    def send(self, *args):
        for client in self.clients:
            if len(args) == 1:
                client.send(args[0])
            elif len(args) == 2:
                client.send(args[0], '')
            elif len(args) == 3:
                client.send(args[0], args[1], args[2])
            elif len(args) == 6:
                client.send(args[0], args[1], args[2], args[3], args[4], args[5])

    def start_server(self):
        while 1:
            client_socket, (ip, port) = self.sock.accept()
            print(f"Client ip={ip} [{port}] connected")
            if 0 not in self.colors:
                connected_client = ConnectedClient(self, client_socket, ip, port, 0, 'user1')
                self.colors.add(0)
            else:
                connected_client = ConnectedClient(self, client_socket, ip, port, 1, 'user2')
            print('clients', len(self.clients))

                #connected_client.start()
            self.clients.add(connected_client)
            if len(self.clients) == 2:
                for client in self.clients:
                    client.start()
                    print(client.color)

address = ("127.0.0.1", 10000)
server = Server(address)
server.start_server()
