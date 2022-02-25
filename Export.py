from Storage import Storage
from Clients import Clients

class Export(Storage, Clients):

    def __init__(self, nameStorage='storage_1_db',phoneClient='None'):
        self.__nameStorage = nameStorage
        self.__phoneClient = phoneClient
        super().__init__(nameStorage)

    def operation(self, nameItem, countItem):
        if isinstance(nameItem,str) and isinstance(countItem, int):
            true_count = 0 - countItem
            super().addPokupka(nameItem,countItem,self.__phoneClient,Storage.updateStorage(self,nameItem,true_count))
        else:
            raise ValueError('Wrong data types: str, int')