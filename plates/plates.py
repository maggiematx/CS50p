def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length of plate
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Initialize variable to track if we have encountered a digit
    has_digit = False

    for i, char in enumerate(s):
        if not char.isalnum():
            return False  # Contains invalid characters

        if char.isdigit():
            if i == 0 or i == 1:
                return False  # Digit in the first two positions
            if char == '0' and not has_digit:
                return False  # First digit is '0'
            has_digit = True

        if has_digit and char.isalpha():
            return False  # Letter after a digit

    return True

if __name__ == "__main__":
    main()


