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

    price=get_price()
    cost=amount*price
    print(f"${cost:,.4f}")

def get_price():
    try:
        response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        o=response.json()
        return o["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        pass

main()
