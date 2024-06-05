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
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    r = requests.get(url, headers=headers).json()
    subscribers = r.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
