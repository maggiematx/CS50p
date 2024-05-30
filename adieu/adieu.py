import inflect
import sys

def main():
    names = get_names()
    farewell(names)

def get_names():
    p = inflect.engine()
    names = []

    print("Enter names (press Ctrl-D to finish):")
    try:
        while True:
            name = input()
            if name:
                names.append(name)
    except EOFError:
        pass

    return names

def farewell(names):
    p = inflect.engine()
    names_str = p.join(names)
    print(f"Adieu, adieu, to {names_str}")

if __name__ == "__main__":
    main()
