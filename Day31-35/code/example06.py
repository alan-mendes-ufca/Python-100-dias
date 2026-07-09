"""Codificação e decodificação com BASE64
0-9A-Za-z+/
1100 0101 1001 0011 0111 0110
00110001 00011001 00001101 00110110
base64
b64encode /b64decode
-------------------------------------
Serialização e desserialização
A serialização transforma objetos em representações de bytes ou texto.
A desserialização reconstrói objetos a partir dessas representações.
Suporte à biblioteca padrão Python:
json - serialização baseada em texto
pickle - serialização baseada em bytes
despejos / cargas"""
import base64
import json
import os

import redis

from example02 import Person


class PersonJsonEncoder(json.JSONEncoder):

    def default(self, o):
        return o.__dict__


def main():
    options = {
        'host': os.getenv('REDIS_HOST', '127.0.0.1'),
        'port': int(os.getenv('REDIS_PORT', '6379')),
        'password': os.getenv('REDIS_PASSWORD'),
        'socket_connect_timeout': 5,
        'socket_timeout': 5,
    }
    if os.getenv('REDIS_TLS', '').lower() == 'true':
        options.update(ssl=True, ssl_cert_reqs='required')
    cli = redis.Redis(**options)
    encoded_data = cli.get('guido')
    if encoded_data is None:
        print('Image "guido" was not found in Redis.')
        return
    data = base64.b64decode(encoded_data)
    with open('guido2.jpg', 'wb') as file_stream:
        file_stream.write(data)
    # with open('guido.jpg', 'rb') as file_stream:
    #     result = base64.b64encode(file_stream.read())
    # cli.set('guido', result)
    # persons = [
    #     Person('Luo Hao', 39), Person('Wang Dachui', 18),
    #     Person('Bai Yuanfang', 25), Person('Di Renjie', 37)
    # ]
    # persons = json.loads(cli.get('persons'))
    # print(persons)
    # cli.set('persons', json.dumps(persons, cls=PersonJsonEncoder))


if __name__ == '__main__':
    main()
