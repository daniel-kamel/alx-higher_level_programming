#!/usr/bin/python3
"""
Uses GitHub's API to get the last 10 commits of a GitHub repository
"""
import requests
from sys import argv


def main():
    """Uses GitHub's API to get the last 10 commits of a GitHub repository"""
    repo = argv[1]
    owner = argv[2]
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(owner, repo),
                     params={'per_page': 10})
    for commit in r.json()[:10]:
        print(commit.get('sha'),
              commit.get('commit').get('author').get('name'))


if __name__ == "__main__":
    main()
