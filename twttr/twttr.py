def main():
    user_input=input("Input: ")
    print(shortened(user_input))

def shortened(text):
    v=["a", "e","i","o","u"]
    nv=""
    for i in text:
        if i.lower() not in v:
            nv += i
    return nv

main()
