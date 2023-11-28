#!/usr/bin/python3
"""This Python script takes in a URL sends a request
to the URL and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    g = requests.get(url)
    if g.status_code >= 400:
        print("Error code: {}".format(g.status_code))
    else:
        print(g.text)
