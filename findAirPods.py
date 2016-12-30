import requests
import json
import sys 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("location", help="Enter US zip code where you want to search")
parser.add_argument("product", help="Enter Apple product code to search (easiest to get this code by adding it to cart)")
args = parser.parse_args()

prod = args.product
prodcode = prod.replace("/", "%2F") #need to do this for the URL 
testZip = args.location

baseUrl = 'http://www.apple.com/shop/retail/pickup-message?parts.0=' + prodcode + '&location='

r = requests.get(baseUrl+testZip)
if r.status_code <> 200:
    print "error"

x = json.loads(r.text)

totResults = len(x['body']['stores'])

for i in range(0,totResults):
    storename = x['body']['stores'][i]['storeName']
    storeavail = x['body']['stores'][i]['partsAvailability'][prod]['pickupSearchQuote']
    storeavail = storeavail.replace("<br/>", " ")
    print 'For store: ' + storename + ' -- ' + storeavail
