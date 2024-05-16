def convert(text_str):
    converted_text=text_str.replace(":)", "🙂").replace(":(", "🙁")
    return converted_text

def main():
   user_input = input("How are you feeling now?")
   converted = convert(user_input)
   print(converted)

if __name__ == "__main__":
    main()

