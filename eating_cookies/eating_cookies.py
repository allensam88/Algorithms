#!/usr/bin/python
# STEP 1: UNDERSTAND
# All possible permutations for 5 cookies
# 1.	1+1+1+1+1
# 2.	1+1+1+2
# 3.	1+1+2+1
# 4. 	1+2+1+1
# 5. 	2+1+1+1
# 6. 	1+2+2
# 7. 	2+1+2
# 8. 	2+2+1
# 9. 	1+1+3
# 10. 	1+3+1
# 11. 	3+1+1
# 12. 	2+3
# 13. 	3+2

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    if n <= 0:
		return 1
	if n > 0:
		return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
