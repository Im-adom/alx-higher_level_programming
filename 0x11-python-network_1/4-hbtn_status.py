#!/usr/bin/python3
"""This Python script fetches https://alx-intranet.hbtn.io/status
using the package requests.
"""

if __name__ == '__main__':
    import requests
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
