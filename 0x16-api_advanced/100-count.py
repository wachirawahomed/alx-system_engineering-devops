#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords.
(case-insensitive, delimited by spaces. Javascript should count as javascript,
but java should not).
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
        Recursively counts keywords in the titles of
        hot articles on a subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.1 (by /u/your_username)'}
    params = {'after': after, 'limit': 100}  # Fetch 100 posts at a time

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            # Convert word_list to lowercase for case-insensitive matching
            word_list = [word.lower() for word in word_list]

            # Initialize the word_count dictionary
            if not word_count:
                word_count = {word: 0 for word in word_list}

            # Count the occurrences of each word in the titles
            for post in posts:
                title_words = post['data']['title'].lower().split()
                for word in word_list:
                    word_count[word] += title_words.count(word)

            # Check if there are more pages to fetch
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                # Sort and print the results
                sorted_word_count = sorted(word_count.items(),
                                           key=lambda kv: (-kv[1], kv[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print(f"{word}: {count}")
        else:
            return None
    except requests.RequestException:
        return None
