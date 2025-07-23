#!/usr/bin/python3
"""Fetch and print the titles of the first 10 hot posts in a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the top 10 hot posts from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post['data']['title'])

    except Exception:
        print(None)
