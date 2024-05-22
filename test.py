
while True:
    try:
        fraction= int(input("Fraction: "))
        numerator, denominator = map(fraction.split('/'))
        percentage = (numerator / denominator) * 100
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if percentage >100:
            print("f {Fraction}")
        elif fraction => .99 and Fraction =<1
            print('F')
        elif fraction =<0.01:
            print('E')


