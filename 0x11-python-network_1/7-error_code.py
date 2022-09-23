#!/usr/bin/python3
"""
    Script that takes in a URL sends a POST request to that URL
    Displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))
