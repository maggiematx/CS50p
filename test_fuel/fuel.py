def main():
     while True:
        try:

            fraction= input("Fraction: ")
            x, y = map(int,fraction.split('/'))

            if x > y:
                raise ValueError

            if 99 <= percentage <= 100:
                print('F')
            elif percentage<=1:
                print('E')
            else:
                print(f"{percentage:.0f}%")
                break

        except (ValueError, ZeroDivisionError):
            pass


def convert(fractioin):

def guage(percentage):
        percentage = (x / y) * 100

