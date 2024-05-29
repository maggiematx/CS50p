from pyfiglet import Figlet
import random
import sys

def main():
    figlet()

def figlet():
    figlet = Figlet()
    user_input=input("Input: ")

    if len(sys.argv)==2 or len(sys.argv)>3:
        sys.exit("Invalid usage")

    elif len(sys.argv)==1:
        output=random.choice(user_input)
        print(f"Output: {output}")

    elif len(sys.argv)==3:
        print(f"Output: {figlet.renderText(output)")

main()
