from datetime import datetime

class Time:

    def __init__(self,name,account_number,balance):
                 self.name=name
                 self.account_number=account_number
                 self.balance=balance

def main():
    obj1 = get_balance()
    print(f"The account balance for {obj1.name} is {obj1.balance}")

def get_balance():
        name="Maggie"
        account_number="12345"
        balance="500"
        return BankAccount(name, account_number,balance)

if __name__== "__main__":
    main()

