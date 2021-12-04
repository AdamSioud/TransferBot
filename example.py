from web3 import Web3
import json
import requests
import math


abi=json.load(open("pyuniswap/abi_files/" + "router.abi"))
erc20_abi = json.load(open("pyuniswap/abi_files/" + "erc20.abi"))
# add your blockchain connection information

eth = 'https://speedy-nodes-nyc.moralis.io/2dffe52a18829bf467200f7a/eth/mainnet'   
web3 = Web3(Web3.HTTPProvider(eth))
print("True if connected to server", web3.isConnected())

tokenAddress = web3.toChecksumAddress(input("Enter ethAdress: "))


erc20balance = 'https://deep-index.moralis.io/api/v2/'+ tokenAddress + '/erc20?chain=eth'

#erc20balance = 'https://deep-index.moralis.io/api/v2/0xE592427A0AEce92De3Edee1F18E0157C05861564/erc20?chain=eth'

#price = 'https://deep-index.moralis.io/api/v2/0xE592427A0AEce92De3Edee1F18E0157C05861564/erc20?chain=eth'


headers = {'x-api-key': '2FH7cpY0wTfzajT3BwaF9eMIEquBABxvhQGlZuZBbAErVuN1Q2bixvJdgFI6N4S6'}


response = requests.request("GET", erc20balance, headers=headers)
 
#getPrice = requests.request("GET", price, headers=headers)
#getP = getPrice.json()
#usdp = getP['usdPrice']
#print(usdp)

resp = response.json()
print(resp)
#print(resp)
for i in resp:
    print("TokenName: " + i["name"])
    print("Symbol: " + i["symbol"])
    print("Address: " + i['token_address'])
    #ethvalue = web3.utils.fromWei(i['balance'], 'ether')
    print("Balance: ", i['balance'])
    print("desimals", i['decimals'])



target_address = Web3.toChecksumAddress("0x198294CEE14776ee126B98875C26d49f9B7f28E4")
answer = input("Do you want to send tokens to " + target_address  + "Enter yes or no: ") 
if answer == "yes": 
    amount = float(input("amount to send:" + "Enter 25, 50, 75 or 100 for respective %: ")) 
    if amount == 25: 
        print("You selected to send 25 percentage of your balance")
        private_key = input("what is your privatekey?")
        for i in resp:
            transaction = {
                "from": web3.toChecksumAddress(tokenAddress),
                "to": web3.toChecksumAddress(target_address),
                "value": i['balance'],
                "gas": 1500000,
                "gasPrice": web3.eth.gasPrice,
                "nonce": web3.eth.getTransactionCount(tokenAddress)
            }
            signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            #get transaction hash
            print(web3.toHex(tx_hash))  
        #for i in resp:
            #web3.eth.contract(web3.toChecksumAddress(i['token_address']),abi=erc20_abi).sendTransaction({ 'from': tokenAddress}).transfer(target_address, i['balance']*0.25)
    elif amount == 50: 
        print("You selected to send 50 percentage of your balance")
        private_key = input("what is your privatekey?")
    elif amount == 75: 
        print("You selected to send 75 percentage of your balance")
        private_key = input("what is your privatekey?")
    elif amount == 100:
        print("You selected to send 100 percentage of your balance") 
        private_key = input("what is your privatekey?")
    else:
        print("Please enter 25, 50, 75 or 100 next time")
elif answer == "no": 
   print("program ended")
else:  
    print("Please enter yes or no.") 