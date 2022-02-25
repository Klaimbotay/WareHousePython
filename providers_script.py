from Providers import Providers
import OCP

def providers_menu():
    while True:
        db = "provider_db"
        x = Providers(db)
        print("Providers\n-------------------------------")
        answer = input(
            'Choose option\n1)Add provider\n2)Del provider\n3)Providers\n-------------------------------\n'
            'esc - exit\n')
        try:
            if answer == '1':
                name = input('Name: ')
                secName = input('Product')
                phone = input('Phone: ')
                x.add(name,secName,phone)
            elif answer == '2':
                x.delete(input('Type provider phone: '))
            elif answer == '3':
                OCP.InfoPrinter('provider_db').show_info()
            elif answer == 'esc':
                return
            else:
                print("Wrong option, be careful")
        except:
            break