def main():
    while true:
    fraction=input("Fraction: ")
    x,y=map(int, fraction.split("/"))
    result=convert(x,y)
    if result is not None:
        percentage=guage(result)
        print(percentage)
        break


def convert(x,y):
        try:
            if y==0:
                raise ZeroDivisionError
            if fraction <=0.01:
                return E
            elif fraction >= 0.99:
                return F
            elif  x>y:
                return None
            else:
                break
        except(ValueError, ZeroDivisonError):
            pass

def gauge(percentage):
    return fraction*100

if__name__=="__main__"
    main()
