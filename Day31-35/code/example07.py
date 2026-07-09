"""Resumos de hash, assinaturas digitais e funções de hash unidirecionais.

Aplicações:
1. Armazenando dados confidenciais como resumos
2. Assinatura de dados para detecção de adulteração
3. Desduplicação no armazenamento em nuvem"""


class StreamHasher():
    """Gerador de resumo."""

    def __init__(self, algorithm='md5', size=4096):
        """Inicializador.
        @params:
            algoritmo - algoritmo de hash
            size - leia o tamanho do pedaço"""
        self.size = size
        cls = getattr(__import__('hashlib'), algorithm.lower())
        self.hasher = cls()
    

    def digest(self, file_stream):
        """Gere uma string de resumo hexadecimal."""
        # data = file_stream.read(self.size)
        # while data:
        #     self.hasher.update(data)
        #     data = file_stream.read(self.size)
        for data in iter(lambda: file_stream.read(self.size), b''):
            self.hasher.update(data)
        return self.hasher.hexdigest()

    def __call__(self, file_stream):
        return self.digest(file_stream)


def main():
    """Ponto de entrada do programa."""
    hasher1 = StreamHasher()
    hasher2 = StreamHasher('sha1')
    hasher3 = StreamHasher('sha256')
    with open('Python-3.7.2.tar.xz', 'rb') as file_stream:
        print(hasher1.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher2.digest(file_stream))
        file_stream.seek(0, 0)
        print(hasher3(file_stream))


if __name__ == '__main__':
    main()
