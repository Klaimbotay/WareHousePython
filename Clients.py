from Verification import Verification
from DataBaseInterfaces import DataBaseInterfaces
from typing import Optional

class Clients(Verification, DataBaseInterfaces):

    def __init__(self, database=None):
        self.database = database

    def addPokupka(self, nameItem, countItem, phone, isOkay):
        with open(f'clients_db','r') as db:
            new_db = db.read()
        if not isOkay:
            return 0
        if not(phone in new_db):
            raise ValueError('There is no such client')

        splitted_db = new_db.split('\n')
        new_db = ''
        for line in splitted_db:
            if phone in line:
               newline = line + f' {nameItem} {countItem}\n'
               new_db += newline
            else:
                new_db += line + '\n'

        with open(f'clients_db','w') as db:
            db.write(new_db)

    def add(self,name,secName,phone):
        if(self.verificate_client(phone)):
            with open(f'clients_db','a') as db:
                db.write(f'{name} {secName} {phone}' + '\n')

    def edit(self,phone):
        with open(f'clients_db', 'r') as db:
            db_old = db.read()
        if f'{phone}' not in db_old:
            print('There is no person with this phone')
            raise ValueError('Such a person does not exist')

        new_name =  input('Name:')
        new_secName = input('Second name:')
        new_phone = input('Phone:')


        splitted_db = db_old.split('\n')
        new_db = ''
        for line in splitted_db:
            if phone in line:
                new_dannie = line.split(' ')
                new_dannie[0] = new_name
                new_dannie[1] = new_secName
                new_dannie[2] = new_phone
                new_db += new_dannie[0] + ' ' + new_dannie[1] + ' ' + new_dannie[2] + '\n'
            else:
                new_db += line + '\n'

        with open(f'clients_db','w') as db_new:
            db_new.write(new_db)

    def delete(self,phone):
        with open(f'clients_db','r') as db:
            new_db = db.read()

        if f'{phone}' not in new_db:
            print('There is no person with this phone')
            raise ValueError('Such a person does not exist')

        splitted_db = new_db.split('\n')
        new_db = ''
        for line in splitted_db:
            if phone in line:
                continue
            else:
                new_db += line + '\n'

        with open(f'clients_db','w') as db_new:
            db_new.write(new_db)

    def info(self):
        with open(f'clients_db','r') as db:
            for line in db:
                print(line,end='')

class MetaSingleton(type):
    _instance : Optional[type] = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Singleton(Clients, metaclass=MetaSingleton):
    def __init__(self, db):
        super().__init__(db)