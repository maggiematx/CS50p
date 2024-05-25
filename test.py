months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

date=input("Date: ")
if "/" in date:
    month, day, year = date.split("/")
else:
    month, day, year = date.replace(",", "").split()

if month in months:
                month = months.index(month) + 1
print(f"{year}-{month:02}-{day:02}")


