
x, y, z = input("Expression: ").split()
x = float(x)
z = float(z)
if y == "+":
    print(f"{x+z:.1f}")
elif y == "-":
    print(f"{x-z:.1f}")
elif y == "*":
    print(f"{x*z:.1f}")
elif y == "/":
    if z != 0:
        print(f"{x/z:.1f}")
    else:
        print("Invalid division.")


