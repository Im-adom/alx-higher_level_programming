#!/usr/bin/python3
"""This Python script takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    g = requests.get(url)
    print(g.headers.get("X-Request-Id"))
