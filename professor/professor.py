import random


def main():
    n = get_level()
    problems = generate_problems(n)
    score = 0

    for x, y in problems:
        correct_answer = x + y
        attempts = 0
        while attempts < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        else:
            print(correct_answer)

    print(f"score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass


def generate_problems(n):
    problems = []
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        problems.append((x, y))
    return problems


def generate_integer(n):
    if n == 1:
        return random.randint(0, 9)
    elif n == 2:
        return random.randint(10, 99)
    elif n == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
