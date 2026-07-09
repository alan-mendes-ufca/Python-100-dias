"""A comunicação entre threads é mais fácil porque eles compartilham memória de processo.
A comunicação entre processos é mais complicada porque o sistema operacional isola a memória.
multiprocessamento.Queue
Threads daemon não bloqueiam o encerramento do processo."""
from threading import Event, Thread
from time import sleep


def output(content, stop_event):
    while not stop_event.is_set():
        print(content, end='', flush=True)
        stop_event.wait(0.1)


def main():
    stop_event = Event()
    threads = [
        Thread(target=output, args=('Ping', stop_event)),
        Thread(target=output, args=('Pong', stop_event)),
    ]
    for thread in threads:
        thread.start()
    sleep(5)
    stop_event.set()
    for thread in threads:
        thread.join()
    print('bye!')


if __name__ == '__main__':
    main()
