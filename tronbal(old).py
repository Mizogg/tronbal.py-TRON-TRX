#Tron Wallet Generator Check API for Balances/totalTransactionCount/frozen Ammount mizogg.co.uk 25/07/21
import ecdsa
import base58
import random
import requests
import json
import atexit
from time import time
from datetime import timedelta, datetime
from Crypto.Hash import keccak
import threading


colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))

def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)

def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))

start = time()
atexit.register(end_log)
log("Start Program")

def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()

def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)

def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak256(pub_key)[-20:]
    addr = base58.b58encode_check(primitive_addr)
    return addr

print(colour_cyan + "tronbal.py---" + colour_red + "Random Scan for TRON TRX Addresses Balances/totalTransactionCount/frozen Ammount----mizogg.co.uk"  + colour_reset + seconds_to_str())
threadCount = input('Best Run on 1 thread to not block API but you can try more : How many threads to run?:  ')
print(colour_purple +"====================Starting search... Please Wait===================="+ colour_reset)

def seek():
    count=0
    while True:
        raw = bytes(random.sample(range(0, 256), 32))
        key = get_signing_key(raw)
        addr = verifying_key_to_addr(key.get_verifying_key()).decode()
        addhex = base58.b58decode_check(addr.encode()).hex()
        publickey = key.get_verifying_key().to_string().hex()
        privatekey = raw.hex()
        count+=1
        bloc = requests.get("https://apilist.tronscan.org/api/account?address=" + addr) #TRON address API
        res = bloc.json()
        balances = dict(res)["balance"] # balance balances tokenBalances transactions transactions_out totalFrozen
        transaction = dict(res)["totalTransactionCount"]
        frozen = dict(res)["totalFrozen"]
        print(colour_cyan + "trponbal.py---" + colour_red + "Random Scan for TRON TRX Addresses Balances/totalTransactionCount/frozen Ammount" + colour_reset) 
        print (colour_green + 'TRON Address Random Scan : ' + colour_reset + str (count) + ' : ' +colour_red + addr + colour_reset) #TRON address display
        print(colour_cyan +'PrivateKey' + ' : ' + colour_red + privatekey + colour_reset)
        print (colour_yellow + ' --Balance = ' +  str(balances)+ '  --TotalFrozen  = ' +  str(frozen) + '  --Transactions = ' +  str(transaction) + colour_reset)   
        print ("Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + colour_cyan + "-tronbal.py " + colour_reset +" : Date&Time" + seconds_to_str(), '\n')
        if int(balances) > 0 or int(transaction) > 0 or int(frozen) > 0:
            print (colour_purple +  ' <================================= WINNER TRON TRX WINNER =================================>' + '\n' +  colour_reset)
            print(colour_cyan + "Matching Key ==== TRON address Found!!!\n PrivateKey: " + colour_reset + privatekey) #TRON address winner
            print (colour_cyan + 'TRON Address Random Scan : ' + str (count) + ' : ' +colour_green + addr + colour_reset)
            print (colour_green + ' --Balance = ' +  str(balances)+ '  --TotalFrozen  = ' +  str(frozen) + '  --Transactions = ' +  str(transaction) + colour_reset) 
            print (colour_purple +  ' <================================= WINNER TRON TRX WINNER =================================>' + '\n' +  colour_reset)
            f=open(u"winner.txt","a")
            f.write('\n==========TRON TRX Address with Balances/totalTransactionCount/frozen Ammount==============')
            f.write('\nPrivateKey (hex) : ' + privatekey)
            f.write('\nPublic Key       : ' + publickey)
            f.write('\nTRON Address     : ' + addr)
            f.write('\nTRON Address(hex): ' + addhex)
            f.write('\n==========TRON TRX Address with Balances/totalTransactionCount/frozen Ammount==============')
            f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====') 
            f.close()
            continue
            
            
threads = []


for i in range(int(threadCount)):
    t = threading.Thread(target=seek)
    threads.append(t)
    t.start()