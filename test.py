date=input("Date: ")
if "/" in date:
    month, day, year = date.split("/")
else:
    month, day, year = date.replace(",", "").split()
print(month, day, year)
