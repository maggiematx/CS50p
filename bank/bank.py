user_input=input("Greeting: ").strip().lower()
if user_input.startswith("hello"):
    print("$0")
elif user_input.startswith("h") and user_input !="hello":
    print("20")
else:
    print("$100")
