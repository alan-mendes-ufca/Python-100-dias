"""Os decoradores geralmente hospedam preocupações transversais.
Esses são recursos usados ​​em muitos lugares, mas separados da lógica central do negócio.
Decoradores são uma forma prática do padrão proxy e da programação orientada a aspectos."""
from functools import wraps
import os
from random import randint
from time import time, sleep

import pymysql


def record(output):

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time()
            ret_value = func(*args, **kwargs)
            output(func.__name__, time() - start)
            return ret_value

        return wrapper

    return decorate


def output_to_console(fname, duration):
    print('%s: %.3f sec' % (fname, duration))


def output_to_file(fname, duration):
    with open('log.txt', 'a') as file_stream:
        file_stream.write('%s: %.3f sec\n' % (fname, duration))


def output_to_db(fname, duration):
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    if not user or password is None:
        raise RuntimeError('Set MYSQL_USER and MYSQL_PASSWORD to enable database logging.')
    options = {
        'host': os.getenv('MYSQL_HOST', '127.0.0.1'),
        'port': int(os.getenv('MYSQL_PORT', '3306')),
        'database': os.getenv('MYSQL_DATABASE', 'test'),
        'charset': 'utf8mb4',
        'user': user,
        'password': password,
        'autocommit': True,
        'connect_timeout': 5,
        'read_timeout': 5,
        'write_timeout': 5,
    }
    ssl_ca = os.getenv('MYSQL_SSL_CA')
    if ssl_ca:
        options['ssl'] = {'ca': ssl_ca, 'check_hostname': True}
    con = pymysql.connect(**options)
    try:
        with con.cursor() as cursor:
            cursor.execute('insert into tb_record values (default, %s, %s)',
                           (fname, '%.3f' % duration))
    finally:
        con.close()


@record(output_to_console)
def random_delay(min, max):
    sleep(randint(min, max))


def main():
    for _ in range(3):
        # print(random_delay.__name__)
        random_delay(3, 5)
    # for _ in range(3):
    #     # Remove the decorator
    # random_delay.__wrapped__(3, 5)


if __name__ == '__main__':
    main()
