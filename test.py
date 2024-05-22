while True:
    try:
        x=int(input("waht's x"))
        break
    except ValueError:
        print('x is not an integer')
    else:
print(f'x is {x}')





