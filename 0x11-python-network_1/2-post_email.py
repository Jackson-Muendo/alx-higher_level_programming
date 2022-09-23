#!/usr/bin/python3
"""
    A script that takes in a URL and email, sends a POST request to the URL
    with email as a parameter and displays the body of the response
    decoded in utf-8
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(req) as resp:
        html = resp.read()
        print("{}".format(html.decode('utf-8')))
