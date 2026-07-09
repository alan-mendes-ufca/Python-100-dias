"""A comunicação entre threads é mais fácil porque eles compartilham memória de processo.
A comunicação entre processos é mais complicada porque o sistema operacional isola a memória.
multiprocessamento.Queue
Threads daemon não bloqueiam o encerramento do processo."""
from threading import Thread
from time import sleep


def output(content):
    while True:
        print(content, end='')


def main():
    Thread(target=output, args=('Ping', ), daemon=True).start()
    Thread(target=output, args=('Pong', ), daemon=True).start()
    sleep(5)
    print('bye!')


if __name__ == '__main__':
    main()
