#!/usr/bin/python3
"""
    Queries Reddit API for top ten
    posts for a given subreddit
"""


def get_user_agent():
    """ create/return a user_agent """
    platform = "linux"
    app_id = "for_science"
    version = "v0.0.1"
    username = "Almost_Irish"
    user_agent = '{}:{}:{} (by /u/{})'.format(
        platform, app_id, version, username
    )
    return user_agent


def recurse(subreddit, hot_list=[], after=None):
    """ query function """
    import requests

    headers = {
        'user-agent': get_user_agent()
    }

    limit = 100
    payload = {
        'limit': str(limit),
        'after': after
    }
    response = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(
            subreddit),
        headers=headers,
        params=payload
    )

    if response.status_code == 404:
        return None
    json = response.json()
    posts = json['data']['children']
    after = json['data']['after']

    length = len(posts)

    if (length == limit):
        return recurse(
            subreddit,
            hot_list + posts,
            after
        )
    return hot_list + posts

def count_words(subreddit, word_list):
    """
        Counts keywords from hot posts
        in a given subreddit
    """

    counts = []
    for word in word_list:
        counts.append(0)

    posts = recurse(subreddit)

    for post in posts:
        title = post['data']['title']
        for index, word in enumerate(word_list):
            if word in title:
                counts[index] += 1

    
    print("words", word_list)
    print("counts", counts)

    return 1
