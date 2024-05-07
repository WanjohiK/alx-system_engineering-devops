#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords """

import requests
from collections import Counter

REDDIT = "https://www.reddit.com/"
HEADERS = {'user-agent': 'my-app/0.0.1'}


def count_words(subreddit, word_list, after="", word_counts=None):
    if word_counts is None:
        word_counts = Counter()

    if after is None:
        # Sort the keywords by count descending then alphabetically ascending
        sorted_counts = sorted(word_counts.items(),
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    url = REDDIT + "r/{}/hot/.json".format(subreddit)
    params = {
        'limit': 100,
        'after': after
    }

    r = requests.get(
            url, headers=HEADERS, params=params, allow_redirects=False)

    if r.status_code != 200:
        return

    try:
        js = r.json()
    except ValueError:
        return

    try:
        data = js.get("data")
        after = data.get("after")
        children = data.get("children")

        for child in children:
            post = child.get("data")
            title = post.get("title").lower()

            # Split the title into words and remove non-alphanumeric characters
            words = [word.strip('.,!?-_') for word in title.split()]

            for word in words:
                if word in word_list:
                    word_counts[word] += 1

    except Exception:
        return

    return count_words(subreddit, word_list, after, word_counts)
