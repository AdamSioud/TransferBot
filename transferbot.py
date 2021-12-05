from web3 import Web3
import json
import requests
import math

#Connection to Ganache (Dummy blockchain)

ganache_url ="HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

#Connection to blockchain 
#Your blockchain connection information
#Uncomment to connect to to real blockchain

# eth = 'https://speedy-nodes-nyc.moralis.io/2dffe52a18829bf467200f7a/eth/mainnet'   
# web3 = Web3(Web3.HTTPProvider(eth))
# print("True if connected to server", web3.isConnected())


#Two dummy wallets with eth, private_key to account_1
#Change to your own

account_1 = "0xB1DAf071ceF5dd2351379cef1B9d065Eb411Fa0E"
account_2 = "0x53b6Eb6E4d8B64dfdA522dFA83B49885BD7Fdf1b"
private_key = "90e466a7cf3e3d198a17ee0593cde001e95bbcd5c62f4c3c4d07fb4e1c5dedec"

#get a nonce

def sendETH():
    nonce = web3.eth.getTransactionCount(account_1)
    #build a transcation


    # sending 10% of account value, by setting value =
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

#un-comment to send ETH
#sendETH()

def checkBalance():
     print("Checking blanace")
     eth = 'https://speedy-nodes-nyc.moralis.io/2dffe52a18829bf467200f7a/eth/mainnet'   
     web3 = Web3(Web3.HTTPProvider(eth))
     print("True if connected to server", web3.isConnected())

     tokenAddress = web3.toChecksumAddress(input("Enter ethAdress: "))

     #You can try this 0xE592427A0AEce92De3Edee1F18E0157C05861564 address
     erc20balance = 'https://deep-index.moralis.io/api/v2/'+ tokenAddress + '/erc20?chain=eth'


     headers = {'x-api-key': '2FH7cpY0wTfzajT3BwaF9eMIEquBABxvhQGlZuZBbAErVuN1Q2bixvJdgFI6N4S6'}


     response = requests.request("GET", erc20balance, headers=headers)


     resp = response.json()
     print(resp)
     print(resp)
     for i in resp:
        print("TokenName: " + i["name"])
        print("Symbol: " + i["symbol"])
        print("Address: " + i['token_address'])
        print("Balance: ", i['balance'])
        print("desimals", i['decimals'])
     return resp

#uncomment to check balance, have to run checkBalance first to get values for sendBep20 for now
checkBalance()

print(checkBalance())
#sending BEP20 tokens

def sendBep20(send, from_adr, to_adr, contractAddress, key, percantage):
    #Just making sure to be connected
    eth = 'https://speedy-nodes-nyc.moralis.io/2dffe52a18829bf467200f7a/eth/mainnet'   
    #abi=json.load(open("pyuniswap/abi_files/" + "router.abi"))
    abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')
    bsc = "https://bsc-dataseed1.binance.org/" 
    web3 = Web3(Web3.HTTPProvider(eth)) 
    print("True if connected to server", web3.isConnected())  
    contractAddress = web3.toChecksumAddress(contractAddress)
    contract = web3.eth.contract(address=contractAddress, abi=abi)
    nonce = web3.eth.getTransactionCount(web3.toChecksumAddress(from_adr))  
    amount = int(send * percantage)
    print(amount)

    # Build a transaction that invokes this contract's function, called transfer
    token_txn = contract.functions.transfer(web3.toChecksumAddress(to_adr), amount,).buildTransaction({
        "gas": 2000000,
        "gasPrice": web3.toWei(50,"gwei"),
        'nonce': nonce,
        })
    
    signed_txn = web3.eth.account.signTransaction(token_txn, private_key=key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction) 
    print(web3.toHex(tx_hash))

adr_from = input("Send from? ")
adr_to =  input("send to? ")
token_to_private_key = input("PrivateKey ")
percantage = float(input("how much of your total portofolio do you want to send?, write in decimal, ex, 0.1 "))

for i in checkBalance():
    send = float(i['balance'])
    contractAddress = web3.toChecksumAddress(i['token_address'])
    sendBep20(send, adr_from, adr_to, contractAddress, token_to_private_key, percantage)
