#!/usr/bin/python
import sys


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    scenarios = []

    if n == 0:
        scenarios = [[]]
        return scenarios

    def helper(results, round):
        for i in plays:
            results.append(i)
            if round == n:
                scenarios.append(results.copy())
            else:
                helper(results, round + 1)

            results.pop()

    helper([], 1)
    return scenarios


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
