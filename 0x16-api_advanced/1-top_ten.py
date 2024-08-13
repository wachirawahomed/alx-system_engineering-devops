#!/usr/bin/python3
"""
A function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Update User-Agent in the headers
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print(None)
        else:
            for post in posts:
                print(post.get('data', {}).get('title'))
 
    except requests.RequestException:
        print(None)
