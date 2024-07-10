def hello(n):
    try:
        p=1/n
        return p
    except ZeroDivisionError:
        print("cant be zero!")
    finally:
        print("bye")
        return p
print(hello(2))
