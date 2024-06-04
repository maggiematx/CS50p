def main():
     while True:
        try:
            user_input= input("Fraction: ")
            print(guage(convert(fraction)))
            break
         except (ValueError, ZeroDivisionError):
            pass

def guage(percentage):
        while True:
            if x > y:
                raise ValueError
            elif 99 <= percentage <= 100:
                return "F"
            elif percentage<=1:
               reurn "E"
            else:
                return f"{percentage:.0f}%"



def convert(fractioin):
    fraction=map(int,user_input.split('/'))
    percentage = (x / y) * 100




if __name__ == "__main__":
    main()
