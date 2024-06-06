class Product:

    def __init__(self,name,price,discount_percentage_rate):
                 self.name=name
                 self.price=price

    def do_hobby(self):
                if self.hobby=="Tennis":
                           print(self.name,"plays tennis")
obj1 = Student("jackson","Tenis")
print(obj1.name)
obj1.do_hobby()
