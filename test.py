
def main():
    user_input=input("")
    text=convert(user_input)
    print(text)

def convert(text):
    text=text.replace(":)", "😐")
    text=return text.replace(":(", "🙁")


main()
