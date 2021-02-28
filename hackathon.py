import math
from bs4 import BeautifulSoup
import requests
# defining a function to convert the amount in dollars to LTC
def dollarToLiteConversion( amountDollars, conversion ):
    amountLite = amountDollars / conversion  #converting amount to liteCoin using conversion rates 

    return amountLite 
#Main code here calling the functions
page = requests.get("https://www.coindesk.com/price/litecoin")
soup = BeautifulSoup(page.content, 'html.parser')
body = soup.body
Price = soup.find_all('div', class_='price-large')
print(Price)
Price1 = Price[0].text
priceNum = float(Price1[ 1: ])
print (type(priceNum))

amountDollars = 100 
amountInLite = dollarToLiteConversion( amountDollars, priceNum )
print ("Awesome! Your amount of $" + str(amountDollars) + " in Litecoin is " + str(amountInLite) +"LTC" )
