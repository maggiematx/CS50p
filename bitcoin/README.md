Developed a Python program, bitcoin.py, that allows the user to specify the number of Bitcoins they wish to buy as a command-line argument. The program performs the following steps:

	1.	Command-Line Argument Handling:
	•	The program expects the user to provide the number of Bitcoins they want to buy as a command-line argument.
	•	It attempts to convert this argument to a float. If the conversion fails, the program exits with an error message using sys.exit.
	2.	Querying the Bitcoin Price:
	•	The program uses the requests library to query the CoinDesk Bitcoin Price Index API at https://api.coindesk.com/v1/bpi/currentprice.json.
	•	The API returns a JSON object containing the current price of Bitcoin in USD.
	•	The program handles potential network or request errors using a try/except block to catch requests.RequestException.
	3.	Calculating and Outputting the Cost:
	•	The program calculates the total cost of the specified number of Bitcoins in USD.
	•	The result is formatted to four decimal places and uses a comma as a thousands separator.
	•	Finally, the program outputs the cost to the user.