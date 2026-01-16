class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
        else: self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient Balance!")
        else: self.__balance = self.__balance - amount

    def getBalance(self):
        return {self.__balance}

accHolder1 = BankAccount("Anil Yadav", 50000)
accHolder1.deposit(10000)
print(accHolder1.getBalance())

accHolder1.deposit(5000)
accHolder1.withdraw(65000)
print(accHolder1.getBalance())

accHolder1.deposit(0)
accHolder1.withdraw(65000)
print(accHolder1.getBalance())
