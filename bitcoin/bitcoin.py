import requests
import sys
import json

def main():

    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")

    try:
        amount=float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    get_price()
    get_amount()
    print(f"${amount:,.4f}")

      amount=get_amount(sys.argv[1])

get_price():
    try:
        response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

def get_amount():
    get_amount=result * (sys.argv[1])
    while true:


        o=resopnse.json()
        for result in o["results"]:
            return result["rate_float"]

    except requests.RequestException:
        pass

