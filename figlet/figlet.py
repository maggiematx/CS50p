from pyfiglet import Figlet
import random
import sys


def main():
    figlet = Figlet()
    figlet.setFont(font=f)
    user_input = input("Input: ")

    if len(sys.argv) == 2 or len(sys.argv) > 3:
        sys.exit("Invalid usage")



    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())


    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font = sys.argv[2]
            if font not in figlet.getFonts():
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")


    print("Output: ", figlet.renderText(user_input))


main()
