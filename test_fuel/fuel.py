def main():
    while True:
        try:
            user_input = input("Fraction: ")
            percentage = convert(user_input)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = map(int, fraction.split('/'))
    if y == 0:
        raise ZeroDivisionError
    elif x>y:
        raise ValueError

    percentage = (x / y) * 100
    return percentage

def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
