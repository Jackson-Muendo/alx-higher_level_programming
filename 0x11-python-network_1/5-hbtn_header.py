#!/usr/bin/python3
"""
    Script that takes in a URL, sends a request to the URL and dsiplays
    value of the variable X-Request-Id
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers.get('X-Request-Id')))
