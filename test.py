class Super:
    def__init__(self):
    self.supVar=1
class Sub(Super):
    def__init__(self):
        super().__init__()
        self.supVar=12

obj=Sub()


print (obj.subVar)
print(obj.supVar)
