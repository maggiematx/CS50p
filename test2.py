class Product:

    def __init__(self,name,price,discount_percentage):
                 self.name=name
                 self.price=float(price)
                 self.discount_percentage=discount_percentage/100

    def get_discount_amount(self):
                discount=self.price*self.discount_percentage
                print("The discount is ", discount)
                return discount

    def get_discount_price(self):
                discount=self.get_discount_amount()
                discount_price=self.price-discount
                print("The discount price is ", discount_price)

obj1 = Product("Stanely 13 Ounce Wood Hammer","500",10)
obj2=Product('National Hardware 3/4" Wire Nails',5.06, 0)

obj1.get_discount_amount()

obj1.get_discount_price()
