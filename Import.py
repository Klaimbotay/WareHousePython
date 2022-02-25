from Storage import Storage
from Providers import Providers

class Import(Storage,Providers):

    def __init__(self, nameStorage='storage_1_db'):
        self.__nameStorage = nameStorage
        super().__init__(nameStorage)

    def operation(self, nameItem, countItem):
        if isinstance(nameItem,str) and isinstance(countItem, int):
            Storage.updateStorage(self,nameItem,countItem)
        else:
            print('Wrong data types: str, int')
            raise ValueError('Wrong data types: str, int')