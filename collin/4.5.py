class A:
    # parent class
    pass

class B(A):
    # Child class of A
    pass

class C(B):
    # Child class of B, which is also a child class of A
    pass
# Create an instance of C
c = C()

print(isinstance(c, A))

"""
The output of the program is:
True

The instance c of class C is part of the inheritance hierarchy that includes class A.
"""

