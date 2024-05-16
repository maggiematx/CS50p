def convert(input_str):
    converted_input=input_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_input

def main():
   user_input = input("How are you feeling now?")
   converted = convert(user_input)
   print(converted)

if __name__ == "__main__":
    main()

