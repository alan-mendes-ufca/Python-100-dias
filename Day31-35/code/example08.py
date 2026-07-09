"""Criptografia e descriptografia.
A criptografia simétrica usa a mesma chave para criptografia e descriptografia.
A criptografia assimétrica usa chaves diferentes, como RSA.
pip instalar pycrypto"""
import base64

from hashlib import md5

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

# # AES key (32 bytes)
# key = md5(b'1qaz2wsx').hexdigest()
# # AES initialization vector
# iv = Random.new().read(AES.block_size)


def main():
    """Ponto de entrada do programa."""
    # Gere um par de chaves.
    key_pair = RSA.generate(1024)
    # Importe a chave pública.
    pub_key = RSA.importKey(key_pair.publickey().exportKey())
    # Importe a chave privada.
    pri_key = RSA.importKey(key_pair.exportKey())
    message1 = 'hello, world!'
    # Criptografar dados.
    data = pub_key.encrypt(message1.encode(), None)
    # Codifique em BASE64 os dados criptografados.
    message2 = base64.b64encode(data[0])
    print(message2)
    # Decodifica em BASE64 os dados criptografados.
    data = base64.b64decode(message2)
    # Descriptografe os dados.
    message3 = pri_key.decrypt(data)
    print(message3.decode())
    # # AES - criptografia simétrica
    # str1 = 'Eu amo todos vocês!'
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # # Encrypt
    # str2 = cipher.encrypt(str1)
    # print(str2)
    # # Decrypt
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # str3 = cipher.decrypt(str2)
    # print(str3.decode())


if __name__ == '__main__':
    main()
