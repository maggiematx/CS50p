import inflect

def main():
    name()

def name():
    while True:
        try:
            user_input=input("Name: ")

            print("Adieu, adieu, to ", user_input)
        name=inflect(user_input)
        except ValueError
            print ("Adieu, adieu, to ", name)
