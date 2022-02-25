import os.path

class Storage():

    def __init__(self, storageName=None):
        self.database = storageName
        if not os.path.exists(f'storage_1_db'):
            raise ValueError('There is no such storage!')

    def updateStorage(self, nameItem,countItem):
        isOkay = True
        with open(f'storage_1_db', 'r') as db:
            __new_data = db.read()

        if nameItem not in __new_data:
            __new_data += f'\n{nameItem} {countItem}'
            with open(f'storage_1_db', 'w') as db:
                db.write(__new_data)

        else:
            with open(f'storage_1_db', 'w') as db:
                __old_data_splitted = __new_data.split('\n')
                __new_data = ''
                for line in __old_data_splitted:
                    if nameItem in line:
                        str_splitted = line.split(' ')
                        __count = int(str_splitted[1])
                        __count += countItem
                        if __count < 0:
                            isOkay = False
                            print('Not enough product in stock use command 5 to check product')
                            __new_data += (f'{nameItem} {__count + (-countItem)}\n')
                        else:
                            __new_data += (f'{nameItem} {__count}\n')
                    else:
                        if len(line) < 1:
                            continue
                        __new_data += (line + '\n')
                db.write(__new_data)
        return isOkay

    def info(self):
        print("Number of products")
        with open(f'storage_1_db', 'r') as db:
            for line in db:
                print(line, end='')