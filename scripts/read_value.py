# interacting with contracts deployed inside our brownie project
# this function read value directly from rinkeby blockchain and is gonna read from contract that already deployed

from brownie import SimpleStorage, accounts, config    #SimpleStorage object is actually array

def read_contract():
    print(SimpleStorage[0])    # brownie knows the contract we deployed because of build/deployment/4 section
    simple_storage=SimpleStorage[-1]   # if we want to interact with the most recent one use SimpleStorage[-1]
    #abi                             # we kno abi from json file in build/deployement/4 folder
    #address                         # same
    print(simple_storage.retrieve())   #15
    
    

def main():
    read_contract()