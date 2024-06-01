import requests
import sys
import json

def main():
    amount=get_amount(sys.argv[1])

    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")
    #if input cannot be converted to a float
    elif:
        sys.exit("Command-line argument is not a number")
    else:
        print(f"${amount:,.4f}")

def get_amount():
    get_amount=result * (sys.argv[1])
    while true:
    try:
        response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" + sys.argv[1])

        o=resopnse.json()
        for result in o["results"]:
            return result["rate_float"]

    except requests.RequestException:

