class A:

     var = 1

     def __init__(self):

         self.x = 1

class B(A):

      def __init__(self):

            super().__init__()

# b is another reference of B()
b = B()


print(hasattr(A,"__init__"))

print(hasattr(B,"__init__"))

print(hasattr(b,"__init__"))

print(hasattr(b,"x"))

print(hasattr(A,"var"))

print(hasattr(b,"var"))

print(hasattr(B,"super"))
