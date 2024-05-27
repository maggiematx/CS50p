def main():
    calculation()


def calculation():
    user_input = int(input("Expression: ")).split(".")

    if user_input[1] in extension:
        print(extension[user_input[1]])
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
