import inflect



def main():
    names = get_names()


def get_names():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = input("Name: ")
            if name:
                names.append(name)

    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
