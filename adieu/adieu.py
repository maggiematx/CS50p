import inflect
import sys

def main():
    names = get_names()
    farewell(names)

def get_names():
    p = inflect.engine()
    names = []

    while True:
        name = input("Name: ")

        if name:
            names.append(name)

        return names
    except EOFError:

def farewell(names):
    p=inflect.engine()
    names_str=p.join(names)
    print(f"Adieu, adieu, to {names_str}")


if __name__ == "__main__":
    main()
