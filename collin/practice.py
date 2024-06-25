class ExampleClass:
                  def __init__(self,first):
                                    self.first = first
                  def set_second(self, second):
                                     self.second = second
o1= ExampleClass(1)
o2 = ExampleClass(2)
o3 = ExampleClass(4)
o2.set_second(3)
o3.third = 5
print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)
