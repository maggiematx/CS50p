import random


def main():
    level=get_level()
    problems=generate_integer(level)
    score=0

    for x,y in problems:
    correct_answer=x+y
    attempts=0
    while attempts<3:
        try:
         user_answer=int(input(f"{x}+{y}= "))
         if user_answer==correct_anser:
            score += 1
            break
            continue
         else:
             print("EEE")
             continue
         #break after three EEE
         braek
         #print the right answer
         print()


    total_score=sum()
    print("Score:, ", total_score)







def get_level():
    n=input["Level: "]
    while True:
        for n in range [1:3]:
            break
        else:
            raise ValueError
    return n


def generate_integer(level):
    #generate n level of int
    x=random.randint(x)>0
    y=random.randint(y)>0
    for n==1,

if __name__ == "__main__":
    main()
