#!/usr/bin/python3
"""
Recursive function to query the Reddit API, parse the titles of all
hot articles, and print a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursively counts occurrences of given keywords in the titles of all
    hot articles for a given subreddit from the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count occurrences for.
        hot_list (list): List to store titles of hot articles
                         (default empty list).
        after (str): Identifier for the starting point of the next page
                     (default None).

    Returns:
        None
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
                count_words(subreddit, word_list, hot_list, after)
            else:
                word_count = {}
                for title in hot_list:
                    words = title.lower().split()
                    for word in words:
                        if word in word_list:
                            word_count[word] = word_count.get(word, 0) + 1
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
        else:
            return
    else:
        return

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)

