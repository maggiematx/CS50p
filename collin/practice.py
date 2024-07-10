def hell(n):
    try:
        p=1/n
    except ZeroDivisionError:
        print("cant be zero!")
    else:
        return p
    finally:
        print("bye")
        return p
