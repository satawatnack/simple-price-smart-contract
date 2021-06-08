# simple-price-smart-contract
create simple smart contract that get price from BandChain and bot program using solidity and web3

## Getting Started
1. setup .env file (example in .env.sample)
2. in src/deploy.py
   ```python
    deploy_contract(os.environ['ADDRESS'], os.environ['PRIVATE_KEY'])
   ```
3. set your contract address in .env
4. in src/botty.py
   ```python
    startBot()
   ```
