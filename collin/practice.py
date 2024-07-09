try:
    m = int("Hello!")
except:
    print("You must enter an integer value.")
try:
    m = int("Hello!")
except Exception as e:
    print(e)
