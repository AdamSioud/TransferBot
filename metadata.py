from web3 import Web3
import datetime
import time
from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError
from datetime import date, timedelta
from time import gmtime, strftime
from time import sleep
from threading import Timer

## Getting CMC API Key

cmc = CoinMarketCapAPI('15d0e64b-c558-4c90-8ede-acf68ad38559')

## Getting CMC ID with CoinMarketCap ID Map

get_last_id = cmc.cryptocurrency_map().data
list_number = 0

## Loop to get last id
for ids in get_last_id:
    #print(untrackedCoins[y])
    id = get_last_id[list_number]["id"]
    list_number += 1

## Last id
print(id)


## The id after

new_id = id + 1


## getting metadata

metadata = cmc.cryptocurrency_info

list_of_ids = ''

### making the next 20 ids and putting it in a string

for x in range(-20,60):
    number = new_id + x
    list_of_ids =  list_of_ids + str(number) +  ','
list_of_ids = list_of_ids[:-1]
print(list_of_ids)


### Putting string into metadata to get metadata of potential coins which is not yet added to cryptomarketcap, up to 20 coins.
### Usally there are 2-3 coins not added, other ids will give error, this error is jumped over
try:
    print(metadata(id=list_of_ids))
except Exception as error:
    e = str(error)
    #print("hello")
    #print("/////////////////////////////")
    data = e[e.find('"id": "')+7:e.find('"":')]
    ## print out data to get erros
    data = data.split(",")
    data = [int(i) for i in data]
    final = [] 
    lst = list_of_ids.split(",")
    lst = [int(i) for i in lst]
    for i in lst:
        if i not in data:
            final.append(i)
    final = [str(i) for i in final]
    final_string = ",".join(final)
    print(metadata(id=final_string))
    #print("/////////////////////////////")
