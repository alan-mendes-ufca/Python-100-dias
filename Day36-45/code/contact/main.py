"""Schema SQL para o banco de dados de contatos.

CREATE DATABASE IF NOT EXISTS address CHARACTER SET utf8mb4;
USE address;

CREATE TABLE IF NOT EXISTS tb_contacter (
    conid INT NOT NULL AUTO_INCREMENT COMMENT 'id',
    conname VARCHAR(31) NOT NULL COMMENT 'name',
    contel VARCHAR(15) NOT NULL DEFAULT '' COMMENT 'phone',
    conemail VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'email',
    PRIMARY KEY (conid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
import os
import re

import pymysql


EMAIL_PATTERN = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
PHONE_PATTERN = re.compile(r'^[0-9+() -]{1,15}$')

INSERT_CONTACTER = """
insert into tb_contacter (conname, contel, conemail) 
values (%s, %s, %s)
"""
DELETE_CONTACTER = """
delete from tb_contacter where conid=%s
"""
UPDATE_CONTACTER = """
update tb_contacter set conname=%s, contel=%s, conemail=%s 
where conid=%s
"""
SELECT_CONTACTERS = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter limit %s offset %s
"""
SELECT_CONTACTERS_BY_NAME = """
select conid as id, conname as name, contel as tel, conemail as email 
from tb_contacter where conname like %s
"""
COUNT_CONTACTERS = """
select count(conid) as total from tb_contacter
"""


class Contacter(object):

    def __init__(self, id, name, tel, email):
        self.id = id
        self.name = name
        self.tel = tel
        self.email = email


def create_connection():
    """Crie uma conexão MySQL com valores configurados pelo ambiente."""
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    if not user or password is None:
        raise RuntimeError('Set MYSQL_USER and MYSQL_PASSWORD before starting the app.')
    try:
        port = int(os.getenv('MYSQL_PORT', '3306'))
    except ValueError as err:
        raise RuntimeError('MYSQL_PORT must be an integer.') from err
    options = {
        'host': os.getenv('MYSQL_HOST', '127.0.0.1'),
        'port': port,
        'user': user,
        'password': password,
        'database': os.getenv('MYSQL_DATABASE', 'address'),
        'charset': 'utf8mb4',
        'autocommit': True,
        'connect_timeout': 5,
        'read_timeout': 5,
        'write_timeout': 5,
        'cursorclass': pymysql.cursors.DictCursor,
    }
    ssl_ca = os.getenv('MYSQL_SSL_CA')
    if ssl_ca:
        options['ssl'] = {'ca': ssl_ca, 'check_hostname': True}
    return pymysql.connect(**options)


def input_contacter_info(allow_empty=False):
    name = input('Name: ').strip()
    tel = input('Mobile: ').strip()
    email = input('Email: ').strip()
    if not name and not allow_empty:
        raise ValueError('Name is required.')
    if len(name) > 31:
        raise ValueError('Name must contain at most 31 characters.')
    if tel and not PHONE_PATTERN.fullmatch(tel):
        raise ValueError('Mobile must contain at most 15 phone characters.')
    if email and (len(email) > 255 or not EMAIL_PATTERN.fullmatch(email)):
        raise ValueError('Enter a valid email address.')
    return name, tel, email


def add_new_contacter(con):
    try:
        name, tel, email = input_contacter_info()
    except ValueError as err:
        print(f'Invalid contact: {err}')
        return
    try:
        with con.cursor() as cursor:
            if cursor.execute(INSERT_CONTACTER,
                               (name, tel, email)) == 1:
                print('Contact added successfully!')
    except pymysql.MySQLError:
        print('Unable to add the contact.')


def delete_contacter(con, contacter):
    try:
        with con.cursor() as cursor:
            if cursor.execute(DELETE_CONTACTER, (contacter.id, )) == 1:
                print('Contact deleted!')
    except pymysql.MySQLError:
        print('Unable to delete the contact.')


def edit_contacter_info(con, contacter):
    try:
        name, tel, email = input_contacter_info(allow_empty=True)
    except ValueError as err:
        print(f'Invalid contact: {err}')
        return
    contacter.name = name or contacter.name
    contacter.tel = tel or contacter.tel
    contacter.email = email or contacter.email
    try:
        with con.cursor() as cursor:
            if cursor.execute(UPDATE_CONTACTER,
                              (contacter.name, contacter.tel,
                               contacter.email, contacter.id)) == 1:
                print('Contact updated!')
    except pymysql.MySQLError:
        print('Unable to update the contact.')


def show_contacter_detail(con, contacter):
    print('Name:', contacter.name)
    print('Mobile:', contacter.tel)
    print('Email:', contacter.email)
    choice = input('Edit this contact? (yes|no) ').strip().lower()
    if choice == 'yes':
        edit_contacter_info(con, contacter)
    else:
        choice = input('Delete this contact? (yes|no) ').strip().lower()
        if choice == 'yes':
            delete_contacter(con, contacter)


def show_search_result(con, cursor):
    contacters_list = []
    for index, row in enumerate(cursor.fetchall()):
        contacter = Contacter(**row)
        contacters_list.append(contacter)
        print('[%d]: %s' % (index, contacter.name))
    if not contacters_list:
        print('No contacts found.')
        return
    choice = input('View contact details? (yes|no) ').strip().lower()
    if choice == 'yes':
        try:
            index = int(input('Enter the index: '))
        except ValueError:
            print('Enter a valid contact index.')
            return
        if 0 <= index < len(contacters_list):
            show_contacter_detail(con, contacters_list[index])
        else:
            print('Contact index is out of range.')


def find_all_contacters(con):
    page, size = 1, 5
    try:
        with con.cursor() as cursor:
            cursor.execute(COUNT_CONTACTERS)
            total = cursor.fetchone()['total']
            while True:
                cursor.execute(SELECT_CONTACTERS,
                               (size, (page - 1) * size))
                show_search_result(con, cursor)
                if page * size < total:
                    choice = input('Continue to the next page? (yes|no) ').strip()
                    if choice.lower() == 'yes':
                        page += 1
                    else:
                        break
                else:
                    print('No more pages.')
                    break
    except pymysql.MySQLError:
        print('Unable to retrieve contacts.')


def find_contacters_by_name(con):
    name = input('Contact name: ').strip()
    if not name:
        print('Contact name is required.')
        return
    try:
        with con.cursor() as cursor:
            cursor.execute(SELECT_CONTACTERS_BY_NAME,
                           ('%' + name + '%', ))
            show_search_result(con, cursor)
    except pymysql.MySQLError:
        print('Unable to search contacts.')


def find_contacters(con):
    while True:
        print('1. View all contacts')
        print('2. Search contacts')
        print('3. Exit search')
        choice = input('Enter your choice: ').strip()
        if choice == '1':
            find_all_contacters(con)
        elif choice == '2':
            find_contacters_by_name(con)
        elif choice == '3':
            break
        else:
            print('Choose 1, 2, or 3.')


def main():
    try:
        con = create_connection()
    except RuntimeError as err:
        print(err)
        return
    except pymysql.MySQLError:
        print('Unable to connect to the contacts database.')
        return
    try:
        while True:
            print('===== Address Book =====')
            print('1. Create a contact')
            print('2. Find contacts')
            print('3. Exit')
            print('===============')
            choice = input('Choose: ').strip()
            if choice == '1':
                add_new_contacter(con)
            elif choice == '2':
                find_contacters(con)
            elif choice == '3':
                print('Thanks for using the address book. Bye!')
                break
            else:
                print('Choose 1, 2, or 3.')
    finally:
        con.close()


if __name__ == '__main__':
    main()
