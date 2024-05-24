def main():
    while True:
        user_input=input("Date: ")
        try:
        if "/" in user_input:
            input_date=convert_slash_format(user_input)
        else:
            input_date=convert_text_format(user_input)
        if input_dateL
            print(input_date)
            break
    except ErrorValue:
        continue

def convert_slash_format(date_str):
    try:
        month, day, year = map(int, date_str.split("/"))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year:04}-{month:02}-{day:02}"
        else:
            raise ValueError
     except ValueError:
        break

def convert_text_format(date_str):
    month=[
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
    try:
        parts=date_str.split()
        month_str=parts[0]
        day=int(part[1].strip(","))
        year=int(part[2])

        if month_str in months and 1<=day <=31:
            month=months.index(month_str)+1
            return f"{year:04}-{month:02}-{date:02}"
        else:
            raise ValueError
    except (ValueError, IndexError):

main()




