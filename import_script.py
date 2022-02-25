from Import import Import

def import_menu():
    try:
        x = Import()
        x.operation(input('Product: '), int(input('Number: ')))
    except:
        print('Something went wrong, please try later')