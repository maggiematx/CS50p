def main():
    while True:
        try:
            user_input = input("Fraction: ")
            percentage = convert(user_input)
            print(guage(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def guage(percentage):
    if percentage > 100:
        raise ValueError("Percentage cannot be greater than 100")
    elif 99 <= percentage <= 100:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"

def convert(fraction):
    x, y = map(int, fraction.split('/'))
    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    percentage = (x / y) * 100
    return percentage

if __name__ == "__main__":
    main()
