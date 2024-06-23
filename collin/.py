class ExampleClass:
             counter = 0
             def __init__(self,first):
                        self.first = first

o1 = ExampleClass(1)
o2= ExampleClass(2)
o3 = ExampleClass(4)

print(o1.__dict__, o1.counter)
print(o2.__dict__, o2.counter)
print(o3.__dict__, o3.counter)
