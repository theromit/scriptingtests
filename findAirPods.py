import requests
import json

baseUrl = 'http://www.apple.com/shop/retail/pickup-message?parts.0=MMEF2AM%2FA&location='
testZip = '95014'

r = requests.get(baseUrl+testZip)
if r.status_code <> 200:
    print "error"

x = json.loads(r.text)

totResults = len(x['body']['stores'])

for i in range(0,totResults):
    storename = x['body']['stores'][i]['storeName']
    storeavail = x['body']['stores'][i]['partsAvailability']['MMEF2AM/A']['pickupSearchQuote']
    storeavail = storeavail.replace("<br/>", " ")
    #print 'For store: ' + x['body']['stores'][i]['storeName'] + ' -- ' + x['body']['stores'][i]['partsAvailability']['MMEF2AM/A']['pickupSearchQuote']
    print 'For store: ' + storename + ' -- ' + storeavail
