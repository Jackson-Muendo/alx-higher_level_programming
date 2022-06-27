#!/usr/bin/python3
""" defines a nqueens"""


import sys

def nQueens(n):

    queens = [0] * n
    print(queens)
    s = n

    while True:
        while(n > 1):
            if valid(queens, n) == True:
                n = n -1
            else:
                queens[n] += 1
                if queens[n] >= s:
                    queens[n] = 0
                    queens[n + 1] += 1
        print("solution")
        print[queens]
        queens[0] += 1
        n = 0

    def valid(queens, n):
        i = n + 1
        while i < s:
            if (queens[i] == queens[n]):
                return False
        i = n + 1
        while i < s:
            x = 1
            if queens[i] == (queens[n] - x):
                return False
            i + 1
            x + 1
        i = n +1
        while i < s:
            x = 1
            if queens[i] == (queens[n] + x):
                return False
            i + 1
            x + 1
        return True

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except (ValueError, TypeError):
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    nQueens(n)
