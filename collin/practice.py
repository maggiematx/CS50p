import random

for i in range(3):  # Loop 3 times
    print("Beginning of loop iteration", i)
try:
    r = random.randint(1, 4)  # r is pseudorandom
    if r == 1:
        print(int("Fred"))  # Try to convert a non-integer
    elif r == 2:
        # Try to assign to a nonexistent index of the empty list
        [] = 5
    else:
        print(3 / 0)  # Try to divide by zero
except ValueError as e:
    print("Problem with value ==>", type(e), e)
except IndexError as e:
    print("Problem with list ==>", type(e), e)
except ZeroDivisionError as e:
    print("Problem with division ==>", type(e), e)
except Exception as e:
    print("Problem with something ==>", type(e), e)
print("End of loop iteration", i)
