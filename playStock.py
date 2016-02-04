"""
   playStock.py
   by Chris Kyle

   This challenge is from /r/DailyProgrammers. See link at
   https://www.reddit.com/r/dailyprogrammer/comments/40h9pd/20160111_challenge_249_easy_playing_the_stock/

"""

import re

prices = open('test', 'r').read()
priceList = re.split('\n| ', prices)

# Remove empty character elements
priceList = [x for x in priceList if x != '']

# delta is the max difference between prices
delta = float(priceList[1]) - float(priceList[0])

# i is the index of the price for buying. j must be two ahead of i
# because we can't buy and sell within one tick.
for i in range(len(priceList)):
    for j in range(i+2, len(priceList)):
        if float(priceList[j]) - float(priceList[i]) > delta:
            delta = float(priceList[j]) - float(priceList[i])
            low = priceList[i]
            high = priceList[j]

print(low, high)
