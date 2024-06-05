#!/usr/bin/python3
"""
Recursive function to query the Reddit API and
return a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves all hot articles for a given subreddit from
    the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store titles of hot articles
                         (default empty list).
        after (str): Identifier for the starting point of the next page
                     (default None).

    Returns:
        list or None: A list containing the titles of all hot articles for
        the given subreddit, or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
