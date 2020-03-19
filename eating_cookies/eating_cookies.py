#!/usr/bin/python
# STEP 1: UNDERSTAND
# Fibonacci Sequence for 5
# 0, 1, 1, 2, 3, 5
# equals 12

# What is actually happening? I think this tree...
#
# 								----START HERE----
# 									enter n = 5
#										|
# 								 n is not 1 or 2
#		________________________________|________________________________________________
#		|								|												|
# 	invoke(2)						invoke(3)										invoke(4)
# 		|								|												|
#   returns 2		 			 n is not 1 or 2					 			n is not 1 or 2
#  (base stop)							|												|
#						________________|________________				________________|________________
#						|				|				|				|				|				|
#					invoke(0)		invoke(1)		invoke(2)		invoke(1)		invoke(2)		invoke(3)
#						|				|				|				|				|				|
#					returns 1		returns 1		returns 2		returns 1		returns 2  	 n is not 1 or 2
#				   (base stop) 	   (base stop) 	   (base stop) 	   (base stop) 	   (base stop)			|
#																										|
#																										|
#																						________________|________________
#																						|				|				|
#																					invoke(0)		invoke(1)		invoke(2)
#								 -----RESULT-----										|				|				|
#					   Add up all the base returns of 1 or 2						returns 1		returns 1		returns 2
#								  Total Sum = 13.							   	   (base stop)	   (base stop) 	   (base stop)

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache={0: 1, 1: 1, 2: 2}):
    # if 1 or 0 zero cookies left, stop eating
    # if n <= 1:
    #     return 1
    # if only 2 cookies left, stop eating
    # if n <= 2:
    #     return 2
    # if more than 2 cookies left, keep on eating
    # eat either 3, 2, or 1 cookies

    if n in cache:
        return cache[n]

    cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
