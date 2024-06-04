
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Current Balance for {self.name}: ${self.balance:}")

# Example usage:
def main():

    obj1 = BankAccount("Maggie", 12345, 500)

    # Display the balance
    obj1.display_balance()

if __name__ == "__main__":
    main()

