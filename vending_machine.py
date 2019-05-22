'''Specification for the project
Given the amount of change that needs to be paid,
we want to generate the list of coins that should be given to a customer.
We want our function to pay the minimum number of coins possible from the below denominations:
100, 50, 20, 10, 5, 2, 1
Build function that will calculate the coins that should be returned by the vending machine to make correct change
'''

'''
Import our byotest framework and create All tests pass message
'''
from byotest import *

usd_coins = [100, 50, 25, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

# We have an optional argument, so if we don't specify a currency, it will default to this argument
def getchange(amount, coins=eur_coins):
    '''
    Refactored code as if statements are no longer needed:
    if amount == 0:
        return []
    
    if amount in coins:
        return [amount]
    '''
    change = []
    # If the coin is less than or equal to the change that we want to return, we can add it to the change
    for coin in coins:
        #While statement ensures that, as long as the coin is less than or equal to the amount, it will carry on adding it
        while coin <= amount:
            # Deduct amount of coin from the amount that we sent in
            amount -= coin
            change.append(coin)
    
    return change

# Use our `tests_are_equal` test to check that when the change required is 0, we get no coins back
tests_are_equal(getchange(0),[])
# When we get some change, we want one coin to be returned
tests_are_equal(getchange(1),[1])
# When we pass in a different coin
tests_are_equal(getchange(2),[2])
# Tests for each of our coin denominations
tests_are_equal(getchange(5),[5])
tests_are_equal(getchange(10),[10])
tests_are_equal(getchange(20),[20])
tests_are_equal(getchange(50),[50])
tests_are_equal(getchange(100),[100])
# If we need change in more than one coin
tests_are_equal(getchange(3),[2,1])
# Testing that different amounts get the right result
tests_are_equal(getchange(7),[5,2])
#Test for when we need more than one denomination of a coin
tests_are_equal(getchange(9),[5,2,2])
#Tests for the ability to override the coin denominators
tests_are_equal(getchange(35, usd_coins),[25, 10])

print("All tests pass")