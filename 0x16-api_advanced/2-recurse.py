#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches titles of all hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.1 (by /u/your_username)'}
    params = {'after': after, 'limit': 100}  # Fetch 100 posts at a time

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            hot_list.extend([post['data']['title'] for post in posts])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None
