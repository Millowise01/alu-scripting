#!/usr/bin/python3
"""Fetch top 10 hot post titles from a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'Mozilla/5.0'}

    try:
        response = requests.get(reddit_url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {}).get('children', [])
        for post in data[:10]:
            print(post['data']['title'])
    except Exception:
        print(None)
