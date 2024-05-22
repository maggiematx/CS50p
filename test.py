
while True:
    try:
        Fraction= int(input("Fraction: "))*100%
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if Fraction >1:
            print("f {Fraction}")
        elif Fraction => .99 and Fraction =<1
            print('F')
        elif Fraction =<0.01:
            print('E')

main()

