# SRP - Single Responsibility Principle

class Verification():

    def verificate_provider(self, name):
        with open('provider_db') as db:
            for stroka in db:
                if f'{name}' in stroka:
                    print("Such a provider already exists")
                    return False
            return True

    def verificate_client(self,phone):
        if len(phone) == 12:
            with open('clients_db','r') as db:
                for stroka in db:
                    if f'{phone}' in stroka:
                        print('Such a person is already registered')
                        return False
        else:
            print('Wrong phone')
            return False
        return True
