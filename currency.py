import requests # API grabber

API_KEY = 'fca_live_ysImQmXgkUPbhKE68CwLozX4KGIh0EKwrmJPfvhb'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES) # convert dict to string
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}" # format URL
    try:
        response = requests.get(url) # whenever you send a request you get a response... it will contain json
        data = response.json()
        return data["data"] # Just access internal dict
    #except Exception as e:
    except:
    #    print(e)
        print("Invalid currency.")
        return None
    
while True:
    base = input("Enter the currency (q for quit): ").upper() # convert to upper case
    
    if base == "Q":
        break    
    
    data = convert_currency(base)
    if not data:
        continue    
    
    del data[base]
    for ticker, value in data.items(): # .items used in dictionaries to iterate over keys and values
        print(f"{ticker}: {value}")