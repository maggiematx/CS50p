def main():
    x=get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x=int(input("waht's x"))
        xcept ValueError:
            print('x is not an integer')
        else:
            break
    return x


main()


