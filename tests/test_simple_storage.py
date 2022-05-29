# be sure the file name start with 'test'
# if you want to use test flags see pytest doc
from brownie import SimpleStorage, accounts

# ==============================================
# we need to test when we deploy our smart contract, it start with 0 in retrieve() function
def test_deploy():
    # Arrange
    account=accounts[0]
    simple_storage=SimpleStorage.deploy({"from": account})
    # Act 
    starting_value=simple_storage.retrieve()
    expected=0
    # Assert
    assert starting_value==expected
    
def test_updating_storage():
    # Arrange
    account=accounts[0];
    simple_storage=SimpleStorage.deploy({"from": account})
    # Act
    simple_storage.store(15,{"from":account})
    expected=15
    retrieve_value=simple_storage.retrieve()
    # Assert
    assert expected==retrieve_value
