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
        if name.lower()==
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
