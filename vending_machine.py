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

'''Challenge 1:
Change the function so that instead of a list of coins, the function works with a dictionary that contains the coin denominations,
and the quantity of each coin available. By default, assume there are 20 of each coin,
but this can be overridden by passing a dictionary to the function as with the previous example.'''
eur_coins = {
    100: 20,
    50: 20,
    20: 20,
    10: 20,
    5: 20,
    2: 20,
    1: 20
    }

usd_coins = {
    100: 20,
    50: 20,
    25: 20,
    10: 20,
    5: 20,
    1: 20
    }

# We have an optional argument, so if we don't specify a currency, it will default to this argument
def get_change(amount, coins=eur_coins):
    """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    `coins` is the set of coins that we need to get change for (i.e. the set
        of available coins)
    Returns a list of coin values
    """
    '''
    Refactored code as if statements are no longer needed:
    if amount == 0:
        return []
    
    if amount in coins:
        return [amount]
    '''
    change = []
    # If the coin is less than or equal to the change that we want to return, we can add it to the change
    # Unlike a list, looping through a dictionary does not keep the order.
    # Therefore we use `sorted()` to sort the order. This will start with the
    # lowest by default, so we use `reverse=True` to start with the highest
    # denomination. The `while` ends when the domination quantity reaches 0.
    # An exception is thrown if there are insufficient coins to give change.
    for coin in sorted(coins.keys(), reverse = True):
        #While statement ensures that, as long as the coin is less than or equal to the amount, it will carry on adding it
        #If a coin that would normally be used to make change isn't available the program should attempt to use smaller coins to make up the change.
        while coin <= amount and coins[coin] > 0:
            # Deduct amount of coin from the amount that we sent in
            amount -= coin
            coins[coin] -= 1
            change.append(coin)
    
    #If it is not possible to make the change with the coins available, the function should raise an error.
    if amount != 0:
        raise Exception("Insufficient coins to give change.")
    
    return change

# Use our `tests_are_equal` test to check that when the change required is 0, we get no coins back
tests_are_equal(get_change(0),[])
# When we get some change, we want one coin to be returned
tests_are_equal(get_change(1),[1])
# When we pass in a different coin
tests_are_equal(get_change(2),[2])
# Tests for each of our coin denominations
tests_are_equal(get_change(5),[5])
tests_are_equal(get_change(10),[10])
tests_are_equal(get_change(20),[20])
tests_are_equal(get_change(50),[50])
tests_are_equal(get_change(100),[100])
# If we need change in more than one coin
tests_are_equal(get_change(3),[2,1])
# Testing that different amounts get the right result
tests_are_equal(get_change(7),[5,2])
#Test for when we need more than one denomination of a coin
tests_are_equal(get_change(9),[5,2,2])
#Tests for the ability to override the coin denominators
tests_are_equal(get_change(35, usd_coins),[25, 10])
# Challenge 1 tests
# Amount we need is 5, there is 1 2c coin and 4 1c coins, we expect to get 1 2c coin and 3 1c coins
tests_are_equal(get_change(5, {2: 1, 1: 4}), [2, 1, 1, 1])
#Insufficient change
test_exception_was_raised(get_change, (5, {2: 1, 1: 2}), "Insufficient coins to give change.")

print("All tests pass")