from sys import exit

if len(sys.argv) < 2:
    exit("Too few arguments")
elif len(sys.argv) > 2:
    exit("Too many arguments")

print("hello, my name is", sys.argv[1])
