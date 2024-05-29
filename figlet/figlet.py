from pyfiglet import Figlet
import random
import sys



def main():
    figlet = Figlet()
    figlet.setFont(font=font)

    if len(sys.argv)==2 or len(sys.argv)>3:
        sys.exit("Invalid usage")

    user_input = input("Input: ")
    print("Output: ", figlet.renderText(user_input))

    if len(sys.argv)==1:
         font=random.choice(figlet.getFonts())

    elif len(sys.argv)==3:
        if sys.argv[1]== "-f" or sys.argv[1]=="--font":
            font=sys.argv[2]
            if font not in figlet.getFonts():
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")



    # Prompt the user for text


    # Output the text in the desired font

main()
