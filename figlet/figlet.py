from pyfiglet import Figlet
import random
import sys

def main():
    figlet()

def figlet():
    figlet = Figlet()

    if len(sys.argv)==2 or len(sys.argv)>3:
        sys.exit("Invalid usage")

    user_input=input("Input: ")
    if len(sys.argv)==1:
        output=random.choice(user_input)
        print(f"Output: {output}")

    elif len(sys.argv)==3:
        if sys.argv[1]== "-f" or sys.argv[1]=="--font":
            sys.exit("Invalid usage")
        else:
            
        print(f"Output: {figlet.renderText(output)}")

main()
