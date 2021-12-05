from web3 import Web3
import json
import requests
import math

ganache_url ="HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

account_1 = "0xB1DAf071ceF5dd2351379cef1B9d065Eb411Fa0E"
account_2 = "0x53b6Eb6E4d8B64dfdA522dFA83B49885BD7Fdf1b"
private_key = "90e466a7cf3e3d198a17ee0593cde001e95bbcd5c62f4c3c4d07fb4e1c5dedec"

#eth = 'https://speedy-nodes-nyc.moralis.io/2dffe52a18829bf467200f7a/eth/mainnet'   
#abi=json.load(open("pyuniswap/abi_files/" + "router.abi"))
#bsc = "https://bsc-dataseed1.binance.org/" 
#w3 = Web3(Web3.HTTPProvider(eth))

#get a nonce

nonce = web3.eth.getTransactionCount(account_1)
#build a transcation

value = int(web3.eth.getBalance(account_1)*0.10)
tx = {
            "nonce": nonce,
            "to": account_2,
            "value": value,
            "gas": 2000000,
            "gasPrice": web3.toWei(50,"gwei")
            }
        
#sign a transaction

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

#account_1 = "0x63156FC12A6da57D25D0f0EfE01894f90F133883"
#account_2 = "0x57A11C44e690e10F4e5A6b9d3e174DE2475a5991"
#private_key = "b412030aa22a018738280e88c17a528a757a385c6544ae701dacb39bad290eec"

# def sendBep20(send, from_adr, to_adr, contractAddress, key):
#     ganache_url ="HTTP://127.0.0.1:7545"
#     web3 = Web3(Web3.HTTPProvider(ganache_url))
    
#     abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')
#     contractAddress = web3.toChecksumAddress(contractAddress)
#     contract = web3.eth.contract(address=contractAddress, abi=abi)
#     nonce = web3.eth.getTransactionCount(web3.toChecksumAddress(from_adr))  
#     amount = 10 * 100000000
#     print(amount)
    
#     # Build a transaction that invokes this contract's function, called transfer
#     token_txn = contract.functions.transfer(web3.toChecksumAddress(to_adr), amount,).buildTransaction({
#         'gas': 210000,
#         'gasPrice': web3.toWei('10', 'gwei'),
#         'nonce': nonce,
#         })
    
#     signed_txn = web3.eth.account.signTransaction(token_txn, private_key=key)
#     tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction) 
#     print(web3.toHex(tx_hash))

# send = 10
# adr_from = "0xB1DAf071ceF5dd2351379cef1B9d065Eb411Fa0E"
# adr_to =  "0x53b6Eb6E4d8B64dfdA522dFA83B49885BD7Fdf1b"
# contractAddress = "0x53b6Eb6E4d8B64dfdA522dFA83B49885BD7Fdf1b"
# token_to_private_key = "90e466a7cf3e3d198a17ee0593cde001e95bbcd5c62f4c3c4d07fb4e1c5dedec"
percantage= input("how much  peranctage of balance do you want to send?")

# sendBep20(send, adr_from, adr_to, contractAddress, token_to_private_key)
#send transaction

#get a transaction hash

#abi=json.load(open("pyuniswap/abi_files/" + "router.abi"))
#erc20_abi = json.load(open("pyuniswap/abi_files/" + "erc20.abi"))






# target_address = Web3.toChecksumAddress("0x198294CEE14776ee126B98875C26d49f9B7f28E4")
# answer = input("Do you want to send tokens to " + target_address  + "Enter yes or no: ") 
# if answer == "yes": 
#     amount = float(input("amount to send:" + "Enter 25, 50, 75 or 100 for respective %: ")) 
#     if amount == 25: 
#         print("You selected to send 25 percentage of your balance")
#         private_key = input("what is your privatekey?")
#         print(web3.toChecksumAddress(i['token_address']))
#         for i in resp:
#             transaction = {
#                 "from": web3.toChecksumAddress(web3.toChecksumAddress(i['token_address'])),
#                 "to": web3.toChecksumAddress(target_address),
#                 "value": i['balance'],
#                 "gas": 1500000,
#                 "gasPrice": web3.eth.gasPrice,
#                 "nonce": web3.eth.getTransactionCount(web3.toChecksumAddress(i['token_address']))
#             }
#             signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
#             web3.eth.send_raw_transaction(signed_tx.rawTransaction)
#             tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
#             #get transaction hash
#             print(web3.toHex(tx_hash))  
#             #web3.eth.contract(web3.toChecksumAddress(i['token_address']),abi=erc20_abi).sendtransaction({ 'from': tokenAddress}).transfer(target_address, i['balance'])
#     elif amount == 50: 
#         print("You selected to send 50 percentage of your balance")
#         private_key = input("what is your privatekey?")
#     elif amount == 75: 
#         print("You selected to send 75 percentage of your balance")
#         private_key = input("what is your privatekey?")
#     elif amount == 100:
#         print("You selected to send 100 percentage of your balance") 
#         private_key = input("what is your privatekey?")
#     else:
#         print("Please enter 25, 50, 75 or 100 next time")
# elif answer == "no": 
#    print("program ended")
# else:  
#     print("Please enter yes or no.") 