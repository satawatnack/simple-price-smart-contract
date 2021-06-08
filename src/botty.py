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
    
    while True:
        try:
            res = set_priceByName("ETH", os.environ['ADDRESS'], os.environ['PRIVATE_KEY'])
            print("Transaction Hash:", res.hex())
            
        except Exception as e: print(str(e))
        
        # sleep 1 hr. == 3600 seconds
        time.sleep(30)

# startBot()

print(get_priceByName("ETH")["price"])