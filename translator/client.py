#! /usr/bin/env python

import sys
import json
import socket
import logging
import concurrent.futures

logging.basicConfig(level=logging.INFO)


class Client:

    def __init__(self, addr, port):
        self.client_socket = socket.socket()
        self.client_socket.connect((addr, port))

    def send(self, data):
        self.client_socket.send(data)

    def listen(self):
        data = b''
        buff = self.client_socket.recv(1024)
        while buff:
            data += buff
            buff = self.client_socket.recv(1024)

        logging.info(f"Received data {data}")
        content = json.loads(data)
        return content;

    def close(self):
        self.client_socket.close()


def translate(data):
    client = Client("localhost", 8090)
    client.send(data)
    answer = client.listen()
    client.close()
    return answer


if __name__ == "__main__":
    content = {
        'text': 'Привет как дела',
        'lang': 'en'
    }
    logging.info(f"Sending message {json.dumps(content)}")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(translate, f"{json.dumps(content)}\r\n".encode("utf8"))
        return_value = future.result()
        print(f"Result: {return_value['text']}")
