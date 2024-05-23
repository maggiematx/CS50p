def main():
    grocery_list()

def grocery_list():
    item_counts={}

    while True:
        try:
            user_input=input("").upper()

            if user_input in item_counts:
                item_counts[user_input] += 1

            else:
                item_counts[user_input] =1

        except EOFError:
            break
    for item in sorted(item_counts):
        print(f"{item_counts[item]} {item}")

main()
