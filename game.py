from random import randint

#pick a random number

number=random.randint(1,n)


while True:
    try:
    user_input=input("Level: ")
    print("Guess: ", user_input)

    if n>0:
        break

    except ValueError:
    pass


    if user_input>number:
        print("Too large!")

    elif user_input<number:
        print("Too smalle!")
    else:
        print("Just right!")

