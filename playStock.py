"""
   playStock.py
   by Chris Kyle

   This challenge is from /r/DailyProgrammers. See link at
   https://www.reddit.com/r/dailyprogrammer/comments/40h9pd/20160111_challenge_249_easy_playing_the_stock/

"""

import re

# Assuming there are no empty lines in the input file, this should work
prices = open('test', 'r').read()
print(prices)
priceList = re.split('\n| ', prices)
print(priceList)

lowest = highest = priceList[0]

# Found this useful for loop on stack exchange for iterating two
# elements at a time. See
# http://stackoverflow.com/a/5389578 for specific answer.
# prices[0::2] means create subset collection of elements that
# index % 2 == 0. Zip then creates a tuple collection from both
# sets.
for i,k in zip(priceList[0::2], priceList[1::2]):
    print(i, k)
