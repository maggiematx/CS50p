from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

def main():
    figlet()

def figlet():

    if len(sys.argv)==2 or len(sys.argv)>3:
        sys.exit("Invalid usage")

    user_input=input("Input: ")
    if len(sys.argv)==1:
        output=random.choice(user_input)
        print(f"Output: {output}")

    elif len(sys.argv)==3, sys.argv[1]== "-f" or sys.argv[1]=="--font":
        print(f"Output: {figlet.renderText(output)}")
        else:
            sys.exit("Invalid usage")

main()
