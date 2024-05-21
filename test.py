def main():
    user_input=input("camelCase: ").strip()
    snakecase=covert(user_input)
    print("snake_case: ", snakecase)

def convert(user_input):
    covert_str=[]
    for c in user_input:
        if c.isupper():
            convert_str.append("_")
            convert_str.appendlower()
        elif c.islower():


    final_str=convert_str



main()
