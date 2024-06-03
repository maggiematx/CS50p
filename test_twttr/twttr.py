def main():
    user_input=input("Input: ")
    print(shorten(user_input))

def shorten(text):
    v=["a", "e","i","o","u"]
    nv=""
    for i in text:
        if i.lower() not in v:
            nv += i
    return nv

if __name__=="__main__":
    main()
