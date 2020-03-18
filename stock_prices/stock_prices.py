#!/usr/bin/python

# STEP 1: UNDERSTAND

# Hints:
# For this problem, we essentially want to find the maximum difference between the smallest and largest prices
# in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price
# by another price that comes _before_ it; it can't come after it in the list of prices.

# trying to find the greatest difference between array values, but only from preceding values
# assume array stock prices are ordered in time sequence, can't use any values AFTER because it's looking into future unknown
# subtract prior indices from current index, one at a time, find the greatest difference, save that value

# Step 2: PLAN

# *****PSEUDO CODE*****
# set initial max value to be 2nd index (arr[1]) minus the previous index (arr[0])
# loop thru each price (i) in prices array
# loop thru prior prices (j) and find price difference
# if price difference is greater than max profit
# then re-assign it to max profit

# ---Example iterations---
# calculate initial max profit = 270 - 1050 = -780
#   i
# [1050, 270, 1540, 3800, 2]
#         j
# 1st iteration: all possible profit values when i = 1 and  j = i + 1 ~~> 490, 1270 | max profit re-assign to 1270
# 2nd iteration: all possible profit values when i = 2 and  j = i + 1 ~~> 2750, 3530, 2260 | max profit re-assign to 3530
# 3rd iteration: all possible profit values when i = 3 and  j = i + 1 ~~> -1048, -268, -1538, -3798 | max profit still at 3530

import argparse


def find_max_profit(prices):
    # figure out the first opening max price
    max_profit = prices[1] - prices[0]
    # loop through each price
    for i in range(1, len(prices)):
        # loop through current prices to compare price differences
        for j in range(i + 1, len(prices)):
            # find difference in current price from prior price, compare to current max profit
            if(prices[j] - prices[i] > max_profit):
                # if result is bigger, re-assign max profit
                max_profit = prices[j] - prices[i]

    return max_profit


# print(find_max_profit([1050, 270, 1540, 3800, 2]))  # should return 3530

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
