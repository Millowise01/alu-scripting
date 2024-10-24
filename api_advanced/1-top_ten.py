#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles 
of the first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    
    Args:
        subreddit: string - the name of the subreddit to query
        
    Returns:
        None - prints the titles or None if subreddit is invalid
    """
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Custom User-Agent to avoid too many requests error
    headers = {
        'User-Agent': 'Custom User Agent 1.0',
        # Disable automatic redirect following
        'Accept': 'application/json'
    }
    
    # Parameters to limit the number of posts
    params = {
        'limit': 10
    }
    
    try:
        # Make GET request to Reddit API
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        
        # Check if subreddit exists (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            posts = response.json().get('data', {}).get('children', [])
            
            # Print titles of first 10 posts
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            # Invalid subreddit or other error
            print(None)
            
    except Exception as e:
        # Handle any errors that might occur
        print(None)
