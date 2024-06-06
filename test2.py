class Student:
    """   Represents a class of students. """
    def __init__(self,name,hobby):
                 self.name=name
                 self.hobby=hobby
    def do_hobby(self):
                if self.hobby=="Tennis":
                           print(self.name,"plays tennis")
obj1 = Student("jackson","Tennis")
print(obj1.name)
obj1.do_hobby()
