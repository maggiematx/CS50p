
while True:
    try:
        fraction= input("Fraction: ")
        numerator, denominator = map(int,fraction.split('/'))
        percentage = (numerator / denominator) * 100

        if denominator == 0:
            raise ZeroDivisionError

        if numerator > denominator:
            raise ValueError

        if 99 <= percentage <= 100:
            print('F')
        elif percentage<=1:
            print('E')
        else:
            print(f"{percentage:}%")
        break

    except (ValueError, ZeroDivisionError):
        pass


