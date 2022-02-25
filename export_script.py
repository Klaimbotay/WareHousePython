from Export import Export

def export_menu():
    try:
        phone = input('Type client phone: ')
        if len(phone) > 1:
            x = Export(phoneClient=phone)
            x.operation(input('Product: '), int(input('Number: ')))
        else:
            print("Wrong phone")
    except:
        print('Something went wrong, please try later')