def main():
    while True:
        try:
            user_input=input("Fraction: ")
            fraction=convert(user_input)
            percentage=gauge(fraction)
            print(gauge(convert(user_input)))
        except (ValueError, ZeroDivisonError)

def convert(fraction):
    x, y= map(int,fraction.split("/"))
    while True:
        try:
            if x > y:
                raise ValueError
            elif y==0:
                raise ZeroDivisonError
            else:
                
