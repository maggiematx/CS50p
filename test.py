def main():
    x = get_int()
    print(f"x is {x}")




def get_int():
    while True:
        try:
            X = int(input("What's X?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()

