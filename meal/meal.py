def main():
    time=input("what time is it now?")
    if 7.0<=converted<=8.0:
        print("breakfast time")
    elif 12.0<=converted <=13.0:
        print("lunch time")
    elif 18.0 <= converted <= 19.0:
        print("dinner time")
    else:
        print("")


def convert(time):
    hours, minutes = time.split(":")
    total_hours=hours+minutes/60.0
    return total_hours

if __name__ == "__main__":
    main()

