def main():
    name=input("what's your name")
    print(f"hello, {name}")

    hello()

def hello(c="world"):
    print("hello,", c)

main()
