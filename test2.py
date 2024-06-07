class BankAccount:

    def __init__(self,name,account_number,balance):
                 self.name=name
                 self.account_number=account_number
                 self.balance=blance


    def get_discount_price(self):
                discount=self.price*self.discount_percentage
                print("The discount is ", discount)
                discount_price=self.price-discount
                print("The discount price is ", discount_price)

obj1 = Product("Stanely 13 Ounce Wood Hammer","500",10)
obj2=Product('National Hardware 3/4" Wire Nails',5.06, 0)



obj1.get_discount_price()
