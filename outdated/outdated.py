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
    

user_month=[
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
    while True:
            input_date=input.strtok(" ")

            for usert_input in user_month:
            if "January" in user_input:
                 return 1
                elif "Feburary" in user_input:
                 return 2

main()




