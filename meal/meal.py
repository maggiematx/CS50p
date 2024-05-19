def main():
    user_input=input()
    if 7<=converted<=8:
        print("breakfast time")
    elif 12<=converted <=13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    return converted



if __name__ == "__main__":
    main()
