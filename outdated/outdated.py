def main():
    user_input=input("Date: ")
    if "/" in user_input:
        input_date=user_input.strtok("/")
    else:
        input_date=convert(user_input)

def convert():
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
    except ErrorValue:
        break
main()




