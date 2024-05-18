expression = input("Expression: ").strip()
x, y, z= expression.split(" ")

x = float(x)
z = float(z)

        # Perform the appropriate arithmetic operation based on the operator
if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    if z!=0:
        result = x / z
    else:
        print("Division by zero is not allowed.")
        print(f"{result:.1f}")

