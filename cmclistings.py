from web3 import Web3
import datetime
import time
from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
from datetime import date, timedelta
from time import gmtime, strftime
from time import sleep
from threading import Timer


cmc = CoinMarketCapAPI('15d0e64b-c558-4c90-8ede-acf68ad38559')

#r = cmc.cryptocurrency_info(symbol='BTC')


#listings = cmc.cryptocurrency_listings_latest()
#for coin in range(100):
    #print(listings.data["date_added"])





untrackedCoins =  cmc.cryptocurrency_map().data
y = 0
#newtoken = 0
checkCoinExist = cmc.cryptocurrency_info
for x in untrackedCoins:
    #print(untrackedCoins[y])
    newtoken = untrackedCoins[y]["id"]
    #print(newtoken)
    #print(untrackedCoins[y]["is_active"])
    y += 1

#untracked = cmc.cryptocurrency_map(listing_status="untracked").data
#print(untracked)
#(our datetime, -> our datetimetime + 5 min) == "first_historical_data"
# (listings.data[coin]["id"],listings.data[coin]["date_added"])  = "first_historical_data"


#function that prints out all times in a day , connects it to "first_historical_data": "2017-07-25T04:30:05.000Z",
#when hit, prints out this value.
#and base on this value get other values

#status1 = cmc.cryptocurrency_map().status
#print(status1)

newtoken += 1
newnewtoken = str(newtoken + 1)
newnewnewtoken =  str(newtoken + 2)
stringtoken = str(newtoken + "," + newnewtoken + "," + newnewnewtoken)
print(checkCoinExist(id=stringtoken))
#while True:
    #print(checkCoinExist(id=y))

#time.sleep(1 - ((time.time()) % 1))

#Solution

def getCoin():
    matchDate = (str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.')))
    newTime = matchDate + "000Z"
    print(newTime)
    for id in range(newtoken, newtoken+5):        
        try:
            #print(x) 
            infoNewCoin = checkCoinExist(id=id)                   
            print(infoNewCoin.data[str(id)]["name"])          
            #if infoNewCoin.data[str(id)]["date_added"] == newTime:
                #print("We did it!!!!!!!!", infoNewCoin)
            #else:
            print("notfound")
        except:
            continue

      
#while True:      
#    getCoin()
#    time.sleep(1)

#address = infoNewCoin.data[str(y)]["platform"]['token_address']
#name = infoNewCoin.data[str(y)]["name"]
#id = infoNewCoin.data[str(y)]["id"]
#print(checkCoinExist(id=y))
#print(infoNewCoin.data[str(y)]["date_added"])
#dateadded  = infoNewCoin.data[str(y)]['data_added']
#print("first information", name, id, address)
#print("Second information", infoNewCoin.data[str(y)])
#print(checkCoinExist(id=y))  

#print("We did it!!!!!!!!", thisvalue)
#print(str(datetime.datetime.now()))
#print(str(current))
#print(checkCoinExist(address = "0x8f081eb884fd47b79536d28e2dd9d4886773f783"))
#print(checkCoinExist(address = "0x51e6ac1533032e72e92094867fd5921e3ea1bfa0"))
#untrackedCoins =  cmc.cryptocurrency_map().data
#print(untrackedCoins[0]["first_historical_data"])

#starttime = time.time()





# newtoken -= 1
# checkCoinExist = cmc.cryptocurrency_info
# infoNewCoin = checkCoinExist(id=newtoken)
# print(infoNewCoin)
# address  = infoNewCoin.data[str(newtoken)]["platform"]['token_address']
# print(address)