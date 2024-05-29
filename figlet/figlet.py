from pyfiglet import Figlet
import random
import sys


def main():
    figlet()

def figlet():
    figlet = Figlet()


    if len(sys.argv) == 2 or len(sys.argv) > 3:
        sys.exit("Invalid usage")



    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())


    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            f = sys.argv[2]
            if f not in figlet.getFonts():
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")

    figlet.setFont(font=font)
    user_input = input("Input: ")

    print("Output: ", figlet.renderText(user_input))


main()
