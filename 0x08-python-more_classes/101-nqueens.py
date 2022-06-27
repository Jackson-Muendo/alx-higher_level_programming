#!/usr/bin/python3
"""Computes all possible solutions to the N-queens puzzle"""


import sys

def n_queen(i):
    """prints a chess board"""
    chess = [['' for c in range(i)] for r in range(i)]
    print(chess)
