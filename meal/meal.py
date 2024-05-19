def convert(time):
    hours, minutes = map(int,time.split(":"))
    total_hours=hours+minutes/60.0
    return total_hours

def main():
    time=input("what time is it now?").strip()
    time_hours=convert(time)
    
    if 7.0<=total_hours<=8.0:
        print("breakfast time")
    elif 12.0<=total_hours <=13.0:
        print("lunch time")
    elif 18.0 <= total_hours <= 19.0:
        print("dinner time")

if __name__ == "__main__":
    main()

