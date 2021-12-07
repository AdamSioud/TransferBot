from pyuniswap.pyuniswap import Token


if __name__ == '__main__':
    #address = input("from wallet address:")
    address = "0xE592427A0AEce92De3Edee1F18E0157C05861564"
    private_key = input("what is your privatekey?")
    #target_address = input("to wallet address:")
    target_address = "0x198294CEE14776ee126B98875C26d49f9B7f28E4"
    amount = float(input("amount to send:"))
    usdt = "0x55d398326f99059ff775485246999027b3197955"
    provider = "https://bsc-dataseed.binance.org/"
    token = Token(usdt, provider=provider)
    token.connect_wallet(address, private_key)
    print("balance2 value", token.balance2(address))
    print("my tokens", token.balanceMoralis)
    tokenss = token.balanceMoralis
    tx = token.transfer(target_address, int(amount * 10**18))
    print(tx.hex())
