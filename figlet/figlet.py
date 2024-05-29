from pyfiglet import Figlet
import random
import sys

def main():
    figlet()

def figlet():
    figlet = Figlet()
    user_input=input("Input: ")

    if len(sys.argv)==0:
    output=random.(user_input)
    print(f"Output: {figlet.renderText(output)}")

main()
