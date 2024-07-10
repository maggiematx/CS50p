a=int(input("what's a? "))
b=int(input("what's b? "))


try:
    p=a/b
    if a<0 or b<0:
        raise ValueError
    print(p)

except ValueError:
    print("wrong input")

else:
    print("right")
    return p
