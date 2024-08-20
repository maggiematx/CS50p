Developed a Python program, `figlet.py`, that allows users to output text in various fonts using the pyfiglet library. The program operates as follows:

- It expects either zero or two command-line arguments:
  - **Zero arguments**: Outputs the text in a random font.
  - **Two arguments**: Outputs the text in a specific font, where the first argument must be `-f` or `--font`, and the second argument must be the name of the font.
  
- The program prompts the user to input a string of text.
- The program then outputs the text in the specified or random font.

If the user provides two command-line arguments but the first is not -f or --font, or the second is not a valid font name, the program exits with an error message using sys.exit.