def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            Fraction= int(input("Fraction: "))*100%
        except ValueError:
            pass
        else:
            if Fraction => .99:
                print('F')
                      if Fraction =<0.01:
                        print('E')
    return x


main()

