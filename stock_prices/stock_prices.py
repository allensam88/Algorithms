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
# 1st iteration
# i starts at 2nd index (arr[1]) and subtracts the previous index (arr[0])
# 	    i
# [1050, 270, 1540, 3800, 2]
# loop thru and find minimum price in prior indices
# set current min price = 1050
# loop thru trimmed array and find differences, then set max profit
# arr[i] = current min price = 270 - 1050 = -780 # negative indicates a loss, no profit
# check result against max profit, if higher, assign to max profit # in this case initial max profit is zero, so assign anyway
# max profit = -780

# 2nd iteration
# 	    	 i
# [1050, 270, 1540, 3800, 2]
# loop thru and find minimum price in prior indices
# set current min price = 270
# loop thru trimmed array and find differences, then set max profit
# arr[i] - current min price = 1540 - 270 = 1270
# check result against max profit, if higher, assign to max profit
# max profit = 1270

# 3rd iteration
# 	    	 	    i
# [1050, 270, 1540, 3800, 2]
# loop thru and find minimum price in prior indices
# set current min price = 270
# loop thru trimmed array and find differences, then set max profit
# arr[i] - current min price = 3800 - 270 = 3530
# check result against max profit, if higher, assign to max profit
# max profit = 3530

# 4th iteration
# 	    	 	    	i
# [1050, 270, 1540, 3800, 2]
# loop thru and find minimum price in prior indices
# set current min price = 270
# loop thru trimmed array and find differences, then set max profit
# arr[i] - current min price = 2 - 270 = -268
# check result against max profit, if higher, assign to max profit
# max profit = 3530

import argparse


def find_max_profit(prices):
    # figure out the first opening max price
    max_profit = prices[1] - prices[0]
    # loop through each price
    for prior_price in range(0, len(prices)):
        # loop through current prices to compare price differences
        for current_price in range(prior_price + 1, len(prices)):
            # find difference in current price from prior price, compare to current max profit
            if(prices[current_price] - prices[prior_price] > max_profit):
                # if result is bigger, re-assign max profit
                max_profit = prices[current_price] - prices[prior_price]

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
