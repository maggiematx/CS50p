def main():
    time=input("what time is it now?").split(":")
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
    total_hours=hours+minutes/60.0
    return total_hours

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
