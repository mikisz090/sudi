import time
from bitcoinaddress import Wallet
import requests

def generate_wallet():
    pk = str(input('Wklej klucz prywatny Twojego portfela: '))
    if pk:
        wallet = Wallet(pk)
    else:
        wallet = Wallet()
    return wallet

def get_balance(address):
    time.sleep(0.1) # Zapobiegnięcie przeciążenia API
    try:
        response = requests.get("https://sochain.com/api/v2/address/BTC/" + str(address))
        return float(response.json()['data']['balance']) 
    except:
        return -1


def bruteForceWallet():
    user123 = 1
    while True:
        try:
            if user123 != 1:
                break
            for i in range(1,100000):
                wallet = Wallet()
                walletAddress = str(wallet.address.__dict__['mainnet'].pubaddr1)
                balance = get_balance(walletAddress)
                if balance == 0.00000000:
                    print("Portfel: " + walletAddress + ", Bilans: " + str(balance) + " BTC")
                if balance > 0.00000000:
                    print("HACKED!")
                    print("Bilans: ", balance)
                    print(wallet)
                    file = open("results.txt","a")
                    file.write(str(wallet) + "\n" "Bilans: " + str(balance) + "\n\n")
                    file.close()
            user123 = input('Wpisz 1 aby kontynuować atak: ')
        except:
            print("Zatrzymywanie...")
            break

