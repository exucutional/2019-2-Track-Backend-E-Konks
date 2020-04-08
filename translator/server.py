#! /usr/bin/env python

import json
import socket
import requests
import logging
from pymemcache.client import base
from pymemcache import fallback

logging.basicConfig(level=logging.INFO)

class Translator:

    def __init__(self, addr, port):
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((addr, port))
        self.socket_server.listen(5)
        self.api_key = "trnsl.1.1.20200407T132632Z.19b1f0ccbc9d05c9.e82289b798de7ce9ec5d52e568274deb2ba54216"
        self.url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
        self.old_cache = base.Client(('memcached', 11211), ignore_exc=True)
        self.new_cache = base.Client(('memcached', 11211))
        self.cache_client = fallback.FallbackClient((self.new_cache, self.old_cache))

    def translate_request(self, args):
        args["key"] = self.api_key
        response = requests.get(self.url, params=args).json()
        if response['code'] == 200:
            return {'status': 'ok', 'text': response['text']}

        return {'status': 'error'}

    def translate(self, params):
        cache_key = f"{params['lang']}-{params['text']}".replace(' ', '_').encode('utf8')
        result = self.cache_client.get(cache_key)
        if result is None:
            result = json.dumps(self.translate_request(params))
            self.cache_client.set(cache_key, result)
            return result
        return result.decode("ascii")

    def listen(self):
        logging.info("Server listening")
        while True:
            client_socket, addr = self.socket_server.accept()
            data = b''
            buff = client_socket.recv(1024)
            while buff:
                data += buff
                if buff.endswith(b'\r\n'):
                    break
                buff = client_socket.recv(1024)

            logging.info(f"Received data {data}")
            content = data.decode("utf8")
            answer = self.translate(json.loads(content))
            logging.info(f"Sending message {answer}")
            client_socket.send(answer.encode("utf8"))
            client_socket.close()


    def close(self):
        self.socket_server.close()


if __name__ == "__main__":
    translator = Translator("0.0.0.0", 8090)
    translator.listen()
    translator.close()
