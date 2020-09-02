import requests 
api_key = '###############'

from_currency = "USD"
to_currency = "INR" 
amount = input('Enter the amount: ')
baseurl = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
main_url = baseurl + '&from_currency='+from_currency+ '&to_currency='+to_currency+'&apikey='+api_key

response = requests.get(main_url)
result = response.json()
key = result['Realtime Currency Exchange Rate']
price = key['5. Exchange Rate']
print('1'+from_currency+'='+price+to_currency)

Famount = int(amount)*float(price)
print(amount,'USD=',Famount,'INR')
