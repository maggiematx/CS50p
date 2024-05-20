def main():
    camel_case=input("camelCase: ").strip()
    snake_case=snake(camel_case)
    print("snake_case: ", snake_case)

def snake(camel_case):
    snake_case_str=[]

    for c in camel_case:
        if c.isupper():
            snake_case_str.append('_')
            snake_case_str.append(c.lower())
        else:
            snake_case_str.append(c)
    return ''.join(snake_case_str)

if __name__ == "__main__":
    main()


