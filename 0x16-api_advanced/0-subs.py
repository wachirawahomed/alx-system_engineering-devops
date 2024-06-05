#!/usr/bin/python3
"""
Script that queries the total number of subscribers for a given Reddit
subreddit.

Args:
    subreddit (str): The name of the subreddit to query.

Returns:
    int: The total number of subscribers for the specified subreddit, or 0 if
    the subreddit is invalid or the request fails.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
