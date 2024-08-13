#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given, it returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyUserAgent/0.1'}

    try:
        # Perform the request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for redirection which indicates invalid subreddit
        if response.status_code == 302:
            return 0

        # Ensure the request was successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)

    except requests.RequestException:
        return 0
