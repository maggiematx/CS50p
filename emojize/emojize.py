import emoji

# Prompt the user to enter text with emoji aliases
user_input = input("Input: ")

# Convert emoji aliases in the user input to actual emojis
output = emoji.emojize(user_input, language='alias')

# Print the converted text
print(f"Output: {output}")
