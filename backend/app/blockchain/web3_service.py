from web3 import Web3
import json
import os

# connect to hardhat blockchain
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if web3.is_connected():
    print("Connected to blockchain")
else:
    print("Blockchain connection failed")

# contract address from deployment
contract_address = Web3.to_checksum_address(
    "0x5FbDB2315678afecb367f032d93F642f64180aa3"
)

# load ABI
artifact_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../smart-contracts/artifacts/contracts/GreenFuel.sol/GreenFuel.json"
    )
)

with open(artifact_path) as f:
    contract_json = json.load(f)
    contract_abi = contract_json["abi"]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

account = web3.eth.accounts[0]

def add_batch_to_blockchain(batch_id):

    tx_hash = contract.functions.addBatch(batch_id).transact({
        "from": account
    })

    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    return receipt.transactionHash.hex()