import random

while True:
    try:
        n=int(input("Level: "))
        if n>0:
            break
    except ValueError:
        pass

number=random.randint(1,n)
0<number<n

while True:
    try:
        user_input=int(input("Guess: "))
        print("Guess: ", user_input)



        if user_input>number:
            print("Too large!")

        elif user_input<number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
            pass
