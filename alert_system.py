class BankAccount:
    def __init__(self,name,balance):
        self.account_holder=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance + amount
        print(f"Deposited {amount} to your account")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Not enough balance")
        else:
            self.balance=self.balance - amount
    def __str__(self):
        return f"Account Holder Name:{self.account_holder} \nBalance: {self.balance}"
obj=BankAccount("John", 3000000)
print(obj)
obj.deposit(5000)
obj.withdraw(7000)
print(obj)
