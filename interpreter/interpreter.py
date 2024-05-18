expression = input("Expression: ").strip()
expression_parts=expression.split(" ")

if len(expression_parts) !=3:
    print("invalid expression format.")
else:
    x,y,z=expression_parts
    
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

