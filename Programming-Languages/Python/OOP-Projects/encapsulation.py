class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected Variable

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
