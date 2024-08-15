#!/usr/bin/python3
"""Module for function to return number of subreddit subscribers."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.
    Args:
        subreddit: subreddit name.

    Returns:
        number of subscribers to the subreddit else 0.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

