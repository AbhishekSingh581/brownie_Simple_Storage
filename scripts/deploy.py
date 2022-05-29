import os
from brownie import accounts, config, SimpleStorage, network   #config: for brownie-config.yaml

def deploy_simple_storage():
    account=get_account()                 # brownie made by local ganache
    
    #---------------------------------
    # for user own account
    # (cmd: brownie accounts new abhishekblockchain-account)->(then enter the private key)->(then password)
    # account=accounts.load("abhishekblockchain-account")
    # print(account)
    
    #-------------------------------------
    # for environment variable 
    # account=accounts.add(os.getenv("PRIVATE_KEY")) #through private key it will give the account address
    # print(account)
    
    #---------------------------------------
    # from brownie-config.yaml
    # account=accounts.add(config["wallets"]["from_key"])   #same as os.getenv
    # print(account)
    
    #=========================================
    print("Contract Deploying.....")
    simple_storage=SimpleStorage.deploy({"from": account})  #brownie smart enough to know its a state change
    # print(simple_storage)
    print("Deployed!")
    #=========================================
    
    
    #=========================================
    stored_value=simple_storage.retrieve()                  #it know its view functiion and we don't need to give account
    print(stored_value)
    #=========================================
    
    
    #========================================
    print("Updating......")
    transaction=simple_storage.store(15,{"from": account})
    updated_stored_value=simple_storage.retrieve() 
    print(updated_stored_value)
    print("Updated!")
    #========================================
    
def get_account():
    if network.show_active()=="development":
        return accounts[0]
    
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()