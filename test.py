date=input("Date: ")
if "/" in date:
    month, day, year = date.split("/")
    print(month, day, year)
