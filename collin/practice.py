def reciprocal(n):
    try:
        p=1/n
    except ZeroDivisionError:
        print("Divison failed")
        p=None
    else:
        print("Everything went fine")
        return p
    finally:
        print("It's time to say goodbye")
        return p
print(reciprocal(0))
