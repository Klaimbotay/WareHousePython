from Clients import *
import OCP


def clients_menu(db):

    while True:
        #Singleton паттерн
        x = Singleton(db)
        print("Clients\n-------------------------------")
        _answer = input(
            'Choose option\n1)Add client\n2)Edit client\n3)Del client\n4)Show clients\n-------------------------------\n'
            'esc - exit\n')
        # Программирование для интерфейса
        try:
            if _answer == '1':
                name = input('Name: ')
                _secName = input('Second name: ')
                _phone = input('Phone number: ')
                x.add(name, _secName, _phone)
            elif _answer == '2':
                x.edit(input('Type client phone: '))
            elif _answer == '3':
                x.delete(input('Type client phone: '))
            elif _answer == '4':
                OCP.InfoPrinter('clients_db').show_info()
            elif _answer == 'esc':
                return
            else:
                print("Wrong option, be careful")
        except:
            break