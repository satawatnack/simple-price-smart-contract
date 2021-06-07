import os
import json
from dotenv import load_dotenv

from web3 import Web3

load_dotenv()
node_provider = os.environ['NODE_PROVIDER']
web3_connection = Web3(Web3.HTTPProvider(node_provider))

def are_we_connected():
    print(web3_connection.isConnected())

contract_abi = json.loads(os.environ['CONTRACT_ABI'])
contract_bytecode = os.environ['CONTRACT_BYTECODE']

def get_nonce(ETH_address):
    return web3_connection.eth.get_transaction_count(ETH_address)

def deploy_contract(name, price, address, signature):
    ethh_contract = web3_connection.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    transaction_body = {
        'nonce': get_nonce(address),
        'gasPrice': web3_connection.eth.gasPrice
    }
    deployment = ethh_contract.constructor(name, price).buildTransaction(transaction_body)
    signed_transation = web3_connection.eth.account.sign_transaction(deployment, signature)
    result = web3_connection.eth.send_raw_transaction(signed_transation.rawTransaction)
    return result
