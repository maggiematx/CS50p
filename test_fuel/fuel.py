def main():
    while true:
        try:
            fraction=input("Fraction: ")
            x,y=map(int, fraction.split("/"))
            if y==0 or x>y:
                continue

            result=convert(x,y)

            percentage=guage(result)
            print(percentage)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(x,y):
        fraction=x/y
        if fraction <=0.01:
            return E
        elif fraction >= 0.99:
            return F
        elif  x>y:
            return None
        else:


def gauge(percentage):
    return round(fraction*100)

if __name__ == "__main__":
    main()
