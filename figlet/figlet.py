from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

def main():
    figlet()

def figlet():

    if len(sys.argv)==2 or len(sys.argv)>3:
        sys.exit("Invalid usage")


    if len(sys.argv)==1:
        output=random.choice(user_input)
        print(f"Output: {output}")

    elif len(sys.argv)==3:
        if sys.argv[1]== "-f" or sys.argv[1]=="--font":
            user_input=input("Input: ")
            print("Output: ", figlet.renderText(output))
        else:
            sys.exit("Invalid usage")

main()
