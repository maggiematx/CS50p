def main():
    list()

def list():
    dict={}

    while True:
        try:
            user_input=input("").upper()

            if user_input in dict:
                dict[user_input] += 1

            else:
                dict[user_input] =1

        except EOFError:
            break
    for item in sorted(dict):
        print(f"{dict[item]} {item}")

main()
