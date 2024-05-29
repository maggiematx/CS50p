import emoji
user_input=input("Input: ")
output=emoji.emojize(user_input, use_aliases=True)
print(f"Output: {output}")
