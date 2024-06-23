class Super:
    def __init__(self,supVar):
        self.supVar = supVar

class Sub(Super):
    def __init__(self,supVar,A):
        super().__init__(supVar)
        self.A = A
obj = Sub(2,5)
print(obj.A)
print(obj.supVar)
