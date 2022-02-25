from Verification import Verification
from DataBaseInterfaces import DataBaseInterfaces


class Providers(Verification, DataBaseInterfaces):

    def __init__(self, database=None):
        self.database = database

    def add(self, name, product, phone):
        if(self.verificate_provider(name)):
            with open('provider_db','a') as db:
                db.write(f'{name} {product} {phone}\n')

    def delete(self, phone):
        with open('provider_db', 'r') as db:
            new_db = db.read()

        if f'{phone}' not in new_db:
            print('There is no supplier with this number')
            raise ValueError('There is no such supplier')

        splitted_db = new_db.split('\n')
        new_db = ''
        for line in splitted_db:
            if phone in line:
                continue
            else:
                new_db += line + '\n'

        with open('provider_db', 'w') as db_new:
            db_new.write(new_db)

    def info(self):
        print("Our providers")
        with open('provider_db', 'r') as db:
            for line in db:
                print(line, end='')