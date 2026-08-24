#!/usr/bin/python3
"""Uses the GitHub API to display a user id with Basic Authentication"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        'https://api.github.com/user',
        auth=(username, password)
    )
    print(response.json().get('id'))
