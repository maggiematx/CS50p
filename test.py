
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Current Balance for {self.name}: ${self.balance:}")


obj1 = BankAccount("Maggie", 12345, 500)

obj1.display_balance()


