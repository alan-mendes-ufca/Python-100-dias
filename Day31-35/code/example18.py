"""Metaconceitos: metadados e metaclasses.
Uma metaclasse descreve como as próprias classes são criadas."""
import threading


class SingletonMeta(type):
    """Metaclasse personalizada."""

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class President(metaclass=SingletonMeta):
    """Presidente (turma única)."""

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f'{self.country}: {self.name}'


def main():
    """Ponto de entrada do programa."""
    p1 = President('Trump', 'USA')
    p2 = President('Obama', 'USA')
    p3 = President.__call__('Clinton', 'USA')
    print(p1 == p2)
    print(p1 == p3)
    print(p1, p2, p3, sep='\n')


if __name__ == '__main__':
    main()
