class BankAccount:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def __str__(self):
        return f"BankAccount(account={self.account}, balance={self.balance:.2f})"
    def transfer(self, target_account, amount):
        if amount > self.balance:
            print("Insufficient funds for transfer")
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
account1 = BankAccount("123456", 100)
account2 = BankAccount("654321", 200)
account1.deposit(50)
account1.withdraw(30)
print(account1)
account1.transfer(account2, 10)
print(account2)