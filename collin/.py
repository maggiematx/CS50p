class Student:
    # Class variable
    school_name = 'ABC School '
    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    # Instance method
    def show(self):
        print('Inside instance method')
        # access using self
        print(self.name, self.roll_no, self.school_name)
# create Object
s1 = Student('Emma', 10)
s1.show()
# access using object reference
print(s1.school_name)
