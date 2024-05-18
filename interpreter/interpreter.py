x, y, z = input("Expression: ").strip().split(" ")

        # Convert the operands to integers
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

