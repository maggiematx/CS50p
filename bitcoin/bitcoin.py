import requests
import sys
import json

def main():
    amount=get_amount(sys.argv)
    
    if len(sys.argv)==1:
        sys.exit("Missing command-line argument")
    #if input cannot be converted to a float
    elif
        sys.exit("Command-line argument is not a number")
    else:
        print(f"${amount:,.4f}")




def get_amount():
    try:
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json" + sys.argv[1])

    o=resopnse.json()
    for result in o["results"]:
        print

    except requests.RequestException:

