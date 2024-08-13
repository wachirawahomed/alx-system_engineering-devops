#!/usr/bin/python3
"""
A function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyUserAgent/0.1'}

    try:
        # Perform the request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for redirection which indicates invalid subreddit
        if response.status_code == 302:
            print(None)
            return
        
        # Ensure the request was successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Check if there are posts and print the titles
        if not posts:
            print(None)
        else:
            for post in posts:
                print(post.get('data', {}).get('title'))

    except requests.RequestException:
        print(None)
