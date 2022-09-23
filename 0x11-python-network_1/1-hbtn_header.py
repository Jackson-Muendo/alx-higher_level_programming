#!/usr/bin/python3
"""
    A script that sends a request to the URL and displays the
    value of the X-Request-Id found in the response
"""

import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print('{}'.format(resp.info().get('X-Request-id')))
