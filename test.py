user_input=input("File name: ").lower().strip()
if user_input=="Hello":
      print(0)
elif user_input.startswith ("h") and user_input != "hello":
      print("$20")
else:
      print("$100")

