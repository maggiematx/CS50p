def main():
    print_square(3)


def print_square(n):
    for i in range(n):
        print_row(n)



def print_row(width):
    print("#" * width)




main()
