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

    if subreddit is None:
        return None

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

    if response.status_code != 200:
        return None
    json = response.json()
    posts = json['data']['children']
    after = json['data']['after']

    if posts == []:
        return None

    kind = posts[0]['kind']
    if kind != "t3":
        return None

    length = len(posts)

    if (length == limit):
        return recurse(
            subreddit,
            hot_list + posts,
            after
        )
    return hot_list + posts
