class A:

    pass

class B(A):
    # Child class of A (does nothing in this example)
    pass

class C(B):
    # Child class of A (does nothing in this example)
    pass
# Create an instance of C
 c = C()

print(isinstance(c, A))


