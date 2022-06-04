#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        t = len(sentence), sentence[0]
    else:
        t = len(sentence), None
    return (t)
