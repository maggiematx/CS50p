class Super:
    def __init__(self):
        self.supVar = 1

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.supVar = 12

obj = Sub()

print(obj.supVar)


