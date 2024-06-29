class A:
     # class attribute
     var = 1

     def __init__(self):
         # Instance attribute
         self.x = 1

# Child class
class B(A):
      def __init__(self):
            # call the parent class's __init__method
            super().__init__()

# b is another instance of calss B
b = B()


print(hasattr(A,"__init__"))

print(hasattr(B,"__init__"))

print(hasattr(b,"__init__"))

print(hasattr(b,"x"))

print(hasattr(A,"var"))

print(hasattr(b,"var"))

print(hasattr(B,"super"))

