def main():
    # Prompt the user for input
    user_input = input("Please enter a sentence: ")

    # Replacing each space with ...
    slow_input = user_input.replace(" ", "...")

    # Output the lowercase input
    print(slow_input)

if __name__ == "__main__":
    main()
