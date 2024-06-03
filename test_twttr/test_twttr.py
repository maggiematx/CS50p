def main():
    user_input=input("")
    print(shortened(user_input))
def shortened(text):
    v=["a","e","i","o","u"]
    nv=""
    for i in text:
        if i.lower() not in v:
            print nv+i
    return nv

