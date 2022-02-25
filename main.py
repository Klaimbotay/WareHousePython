from time import sleep
from clients_menu import *
from storage_script import *
from providers_script import *
from export_script import *
from import_script import *
from exit import *

mainMenuHeader = "\nMain Menu\n-------------------------------"
mainMenuBody = 'Please, choose one option...\n' \
               '1)Clients\n' \
               '2)Export\n' \
               '3)Import\n' \
               '4)Providers\n' \
               '5)Storage\n' \
               '-------------------------------\n' \
               'esc - exit\n'

notExceptedError = "Something went wrong, please try later"
missedKey = "Wrong option, be careful\n"
waitMsg = "Please wait...\n"

loop = True

timeout = 2

while loop:
    print(mainMenuHeader)
    option = input(mainMenuBody)

    try:
        if option == '1':
            while True:
                db = input("Please choose database:") or None
                if db is None:
                    continue
                else:
                    break
            clients_menu(db)
        elif option == '2':
            export_menu()
        elif option == '3':
            import_menu()
        elif option == '4':
            providers_menu()
        elif option == '5':
            storage_menu()
        elif option.lower() == 'esc':
            loop = exitFromApp()
            break
        else:
            print(missedKey, end='')
            print(waitMsg, end='')
            sleep(timeout)
    except:
        print(notExceptedError)
        exit()