#!/usr/bin/python

# Example permutations for 20 cents:
# 1. 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1
# 2. 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+5
# 3. 1+1+1+1+1+1+1+1+1+1+5+5
# 4. 1+1+1+1+1+1+1+1+1+1+10
# 5. 1+1+1+1+1+5+5+5
# 6. 1+1+1+1+1+5+10
# 7. 5+5+5+5
# 8. 5+5+10
# 9. 10+10

import sys


def making_change(amount, denominations):
    total = [0] * (amount + 1)
    total[0] = 1
    for coin in denominations:
        for index in range(coin, amount + 1):
            total[index] += total[index - coin]
    return total[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
