import os
import json
from dotenv import load_dotenv

from web3 import Web3

from bandChain import BandChain

load_dotenv()

node_provider = os.environ['NODE_PROVIDER']
web3_connection = Web3(Web3.HTTPProvider(node_provider))

contract_abi = json.loads(os.environ['CONTRACT_ABI'])
contract_address = os.environ['CONTRACT_ADDRESS']

def are_we_connected():
    print(web3_connection.isConnected())

def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)

def get_priceByName(coinName):
    contract = web3_connection.eth.contract(address=contract_address, abi=contract_abi)
    rid, price = contract.functions.GetPriceByName(coinName).call()
    return { "rid": rid, "price": price }

def set_priceByName(coinName, owner, signature):
    # get price from BandChain
    bandChain = BandChain("to da moon", "band-laozi-testnet1", "http://rpc-laozi-testnet1.bandchain.org")
    res = bandChain.requestCoinData(coinName)

    contract = web3_connection.eth.contract(address=contract_address, abi=contract_abi)

    #ethereum network work in Wei then convert ether to wei
    transaction_body = {
        'nonce': get_nonce(owner),
        'gasPrice': web3_connection.eth.gasPrice
    }

    function_call = contract.functions.SetPriceByName(res["rid"], res["coinName"], res["price"]).buildTransaction(transaction_body)
    signed_transaction = web3_connection.eth.account.sign_transaction(function_call, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result
