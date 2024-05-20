def main():
    user_input=input("Input: ")
    print(shortened(user_input))

def shortened(text):
    v=["a", "e","i","o","u"]
    nv=""
    for char in text:
        if char.lower() not in v:
            nv += char
    return nv

main()
