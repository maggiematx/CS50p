def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length of plate (2-6 characters)
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Track if a digit has been encountered
    has_digit = False


    for char in s:
        if not char.isalnum():
            return False  # Contains invalid characters

        if char.isdigit():
            if char == '0' and not has_digit:
                return False  # First digit is '0'
            has_digit = True

        if has_digit and char.isalpha():
            return False  # Letter found after a digit

    return True

if __name__ == "__main__":
    main()
