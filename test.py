
while True:
    try:
        fraction= int(input("Fraction: "))
        numerator, denominator = map(fraction.split('/'))
        percentage = (numerator / denominator) * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if 99 <= percentage <= 100:
            print('F')
        elif percentage<=1:
            print('E')
        else:
            print(f"{percentage:}%")
        break


