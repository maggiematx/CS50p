def convert(input_str)
    input=input_str.replace(":)", "🙂").replace(":(", "🙁")
    return input

def main():
   user_input = str(input("How are you feeling now?"))
   converted = convert(user_input)
   print(converted)

if __name__ == "__main__":
    main()

