def main():
    while True:
        try:
            user_input=input("Fraction: ")
            fraction=convert(user_input)
            percentage=gauge(fraction)
            print(gauge(convert(user_input)))
        except:
            raise  ValueError

def convert(fraction):
    
