class Prsn:
    def __init__(self, name, personal_code):
        self.__name = name
        self.__personal_code = personal_code
        self.accounts = []
    def add_accounts(self,banks):
        self.accounts.append(banks)
        
    def get_accounts(self):
        print(self.accounts)
        
    def get_info(self):
        print(self.__name)
        print(self.__personal_code)
class Client(Prsn):
    def __init__(self,email,phone,name, personal_code):
        
        self.__email = email
        self.__phone = phone
        self.client_type = "regular"
        super().__init__( name, personal_code)
    def account_summary(self,ac):
        if ac <= 1000:
            self.client_type = "regular"
        elif ac > 1000:
            self.client_type = "premium"
        else:
            self.client_type = "business"
        return
        print(self.__email)
        print(self.__phone)
        print(self.__client_type)
        print(self.__personal_code)
        
class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance
    def add(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("not enoughf money")
    def getbalance(self):
        print(self.__balance)
    def get_account_number(self):
        print(self.__account_number)

prsn = Prsn("name1",123)
prsn.add_accounts("bank")
prsn.get_info()
bc = BankAccount(228,0)
bc.add(2200)
bc.getbalance()
ppl = Client("email1","phone1","name1",123)
ppl.account_summary(bc)