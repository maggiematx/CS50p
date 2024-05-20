def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not starts_with_two_letters(s):
        return False
    if not contains_only_letters_and_numbers(s):
        return False
    if not numbers_at_end(s):
        return False
    if has_invalid_characters(s):
        return False
    return True


main()
