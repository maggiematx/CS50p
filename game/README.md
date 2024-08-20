Developed a Python program, `game.py`, that operates as follows:

1. **Prompt for Level**: The program prompts the user to input a level, which should be a positive integer. If the user does not input a positive integer, the program will keep prompting until a valid input is provided.

2. **Generate a Random Number**: Once a valid level is entered, the program randomly generates an integer between 1 and the entered level (inclusive) using the random module.

3. **Prompt for Guess**: The program prompts the user to guess the generated integer. If the guess is not a positive integer, the program will continue prompting until a valid guess is provided.

4. **Feedback Loop**:
   - If the guess is smaller than the generated number, the program outputs "Too small!" and prompts the user to guess again.
   - If the guess is larger than the generated number, the program outputs "Too large!" and prompts the user to guess again.
   - If the guess is exactly the same as the generated number, the program outputs "Just right!" and then exits. 

This program continues the guessing loop until the user correctly guesses the randomly generated number.