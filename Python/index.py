#!/usr/bin/python
import requests
from solutions import *

REGISTER_URL = 'http://challenge.code2040.org/api/register'
TOKEN = '15700ed71f8fccbcbe8b7e85b3650967'
GITHUB = 'https://github.com/DavidTofu/code2040.git'
ENDPOINTS_AND_SOLUTIONS = [
    ("http://challenge.code2040.org/api/reverse", reverse_string),
    ("http://challenge.code2040.org/api/haystack", find_in_haystack),
    ("http://challenge.code2040.org/api/prefix", find_all_unprefixed),
    ("http://challenge.code2040.org/api/dating", add_seconds_to_date)
]


def register():
    """Register to start API challenge"""
    requests.post(REGISTER_URL, json={'github': GITHUB, 'token': TOKEN})


def solve(url, func):
    """
    Solve the challenge specified by the url by passing the response url to
    func and posting that to url + '/validate'
    """
    print("Solving " + func.__name__ + '...')

    # Get challenge
    response = requests.post(url, json={'token': TOKEN})
    if response.status_code != 200:
        raise Exception("Fetching challenge for " + func.__name__ +
                        " faied with status code: " + response.status_code +
                        " and message: '" + response.text + "'")

    # Solve challenge
    solution = func(response.text)
    solution['token'] = TOKEN               # Add API token to post data

    # Post solution
    response = requests.post(url + '/validate', json=solution)
    if response.status_code != 200:
        raise Exception("Answering " + func.__name__ +
                        " failed with code " + str(response.status_code) +
                        " and message " + response.text)
    else:
        print("Solved " + func.__name__ + "!")


def main():

    register()

    for url, func in ENDPOINTS_AND_SOLUTIONS:
        solve(url, func)


if __name__ == '__main__':
    main()
