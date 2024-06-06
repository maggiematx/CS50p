class Product:
   def __init__( self,name ,price,discountpercent):
                   self.name=name
                   self.price=price
                   self.discountpercent= discountpercent
   def getdiscountamount(self):
                   a=self.price*self.discountpercent
                   print("The discount is ",a)
                   b=self.price-a
                   print("Discounted price for this product is",b)
obj1=Product("TV",500,.10)
obj1.getdiscountamount()
