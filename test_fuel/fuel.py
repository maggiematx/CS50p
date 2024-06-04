def main():
    fraction=input("Fraction: ")
    x,y=map(int, fraction.split("/"))
    result=convert(x,y)
    percentage=guage(result)
    print(percentage)


def convert(fraction):
    while true:
        try:
            if fraction <=0.01:
                return E
            elif fraction >= 0.99:
                return F
            else  x>y:
                

        except(ValueError, ZeroDivisonError):
            pass

def gauge(percentage):
    return fraction*100

if__name__=="__main__"
    main()
