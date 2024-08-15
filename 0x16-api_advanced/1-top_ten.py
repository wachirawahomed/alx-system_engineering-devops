#!/usr/bin/python3
"""Module for task 1"""
import requests


def top_ten(subreddit):
    """
        return top ten titles for a given subreddit.
        return None if invalid subreddit given.
    """
    # get user agent
    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
