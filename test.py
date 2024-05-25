date=input("Date: ")
if "/" in date:
    month, day, year = date.split("/")
else:
    month, day, year = date.replace(",", "").split()
    
if month in months:
                month = months.index(month) + 1
            else:
                continue
