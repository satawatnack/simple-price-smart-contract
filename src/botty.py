import time
import os
from dotenv import load_dotenv

import requests
import json

from interact import set_priceByName, get_priceByName

load_dotenv()

# parameters for get ETH/USD price
parameters = {
    "ids": "ethereum",
    "vs_currencies": "usd"
}

def startBot():
    priceBefore = get_priceByName("ETH")
    
    while True:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/simple/price", params=parameters)
            if (response.status_code == 200):
                data = json.loads(response.text)
                ethPrice = int(data["ethereum"]["usd"])
                if (priceBefore != ethPrice):
                    print('{} ETH/USD -> New price!!! HOLD Ethereum :D'.format(ethPrice))
                    set_priceByName("ETH", ethPrice, os.environ['ADDRESS'], os.environ['PRIVATE_KEY'])
                    priceBefore = ethPrice
                else:
                    print('{} ETH/USD -> Are you a stablecoin?'.format(priceBefore))

        except Exception as e: print(str(e))
        
        # sleep 1 hr. == 3600 seconds
        time.sleep(60)