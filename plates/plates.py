def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length of plate
    if len(s) >1 and len(s) <7:
        return True

    # Check if the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check for valid characters and that numbers are at the end
    has_digit = False
    for i, char in enumerate(s):
        if not char.isalnum():
            return False
        if char.isdigit():
            if char == '0' and (i == 2 or i == 3):  # First digit cannot be '0'
                return False
            has_digit = True
        if has_digit and char.isalpha():
            return False  # Numbers cannot be in the middle

    return True

if __name__ == "__main__":
    main()
