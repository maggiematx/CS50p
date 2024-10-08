def main():
    while True:
        user_input=input("Date: ")
        try:
            if "/" in user_input:
                input_date=convert_slash_format(user_input)
            else:
                input_date=convert_text_format(user_input)

            if input_date:
                print(input_date)
                break

        except ValueError:
            pass

def convert_slash_format(date_str):
    try:
        month, day, year = map(int, date_str.split("/"))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year:04}-{month:02}-{day:02}"
        else:
            raise ValueError
    except ValueError:
        return None

def convert_text_format(date_str):
    months=[
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
        if len(parts)!=3 or ',' not in parts[1]:
            raise ValueError
        month_str=parts[0]
        day_str=parts[1].strip(",")
        day=int(day_str)
        year=int(parts[2])

        if month_str in months and 1<=day <=31:
            month_index=months.index(month_str)+1
            return f"{year:04}-{month_index:02}-{day:02}"
        else:
            raise ValueError
    except (ValueError, IndexError):
        pass

main()




