""" bitcoin task (I forgot to put this in the last ones,
but I did them all by myself. I'm just trying to follow some
aesthetic principles) """

# importing libs
import sys
import requests

# getting file and finding the current btc price
rate = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
price = rate['bpi']['USD']['rate']
# formatting the prie to float
price = float(price.replace(',',''))
# not sure why i'm using htis but it was on the template hehe
try:
    price = float(sys.argv[1]) * price
    # formatting my value so it matchs the expected output
    price = f"${price:,.4f}"
    # printing with no new line
    print(price,end='')
# again, just letting this because it was on the template
except requests.RequestException:
    pass
