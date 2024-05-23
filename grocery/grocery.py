def main():
    list():

def list():
    dict={}

    while True:
        try:
            user_input=input("").upper()

            if user_input in dict:
                dict[user_input] += 1

            else:
                dict =1

        except EOFError:
            break
    print("item, count[dict],sep=", ")

