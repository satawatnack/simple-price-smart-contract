import requests, time

from pyband.pyband import Client
from pyband.pyband.obi import PyObi
from pyband.pyband.message import MsgRequest, MsgSend
from pyband.pyband.wallet import PrivateKey
from pyband.pyband.transaction import Transaction

class BandChain:

    def __init__(self, MNEMONIC, CHAIN_ID, ENDPOINT):
        self.MNEMONIC = MNEMONIC
        self.CHAIN_ID = CHAIN_ID
        self.ENDPOINT = ENDPOINT
    
    def requestCoinData(self, coinName):
        client = Client(self.ENDPOINT)
        PK = PrivateKey.from_mnemonic(self.MNEMONIC)
        sender = PK.to_pubkey().to_address()
        account = client.get_account(sender)
        account_num = account.account_number
        sequence = account.sequence

        obi = PyObi("{symbols:[string],multiplier:u64}/{rates:[u64]}")
        calldata = obi.encode({"symbols": [coinName], "multiplier": 1})

        msg = MsgRequest(
            37,
            calldata,
            16,
            10,
            "Fooo testing bar",  # client id
            [],
            200000,
            1000000,
            sender,
        )

        txn = (
            Transaction()
            .with_messages(msg)
            .with_account_num(account_num)
            .with_sequence(sequence)
            .with_chain_id(self.CHAIN_ID)
            .with_gas(2000000)
            .with_fee(0)
        )

        raw_data = txn.get_sign_data()
        signature = PK.sign(raw_data)
        raw_txn = txn.get_tx_data(signature, PK.to_pubkey())

        # Relay
        txid = client.send_tx_block_mode(raw_txn).tx_hash

        res = requests.get(self.ENDPOINT + "/txs/" + txid.hex())
        res.raise_for_status()

        events = res.json()["logs"][0]["events"]
        rid = events[2]["attributes"][0]["value"]

        time.sleep(15)

        request = client.get_request_by_id(rid)
        output = obi.decode_output(request.result.result)

        return {"rid": int(rid), "coinName": coinName, "price": output["rates"][0]}
