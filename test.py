def main():
    x=input("what's the number?")
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(number):
    if number % 2==0:
        return True
    else:
        return False

main()

