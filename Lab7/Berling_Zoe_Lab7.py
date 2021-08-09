"""Zoe Berling Algorithms Lab 7 NCoinsDynamicProgramming"""
# Below are two algorithms (DAC and DP) to compute the
# minimum number of coins required to produce A cents worth of change
# The DP version also prints out the coins needed to produce this min
from time import time
# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins
        # If we can give change
            if (amount - currentCoin) >= 0:
            # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
        # Keep the best
            minCoins = min(minCoins, currentMin)
        return minCoins
# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    # Create the initial tables
    coinsUsed = [0]*(amount+1) # list to track number of coins
    coinmin = [0]*(amount+1)
    coinsNeeded = []  # return this list based on amount
    # coins.sort()
    # Fill in the base case(s)
    for cents in range(amount + 1):
        count = cents
        newCoin = 1
        for j in [c for c in coins if c <= cents]:
            if coinmin[cents - j] + 1 < count:
                count = coinmin[cents - j] + 1
                newCoin = j
        coinmin[cents] = count
        coinsUsed[cents] = newCoin
        # print(newCoin)
    startingcoin = amount
    while startingcoin > 0:  #  return coins needed
        mycoin = coinsUsed[startingcoin]
        coinsNeeded.append(mycoin)
        startingcoin -= mycoin

    return coinmin[amount], coinsNeeded


C = [1,5,10,12,25] # coin denominations (must include a penny)
A = int(input('Enter desired amount of change: '))
assert A>=0
print("DAC:")
t1 = time()
numCoins = DACcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
print()
print("DP:")
t1 = time()
numCoins, coinsNeeded = DPcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
print("coins needed: ", coinsNeeded)

