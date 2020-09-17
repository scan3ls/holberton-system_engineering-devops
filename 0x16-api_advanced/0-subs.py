#!/usr/bin/python3
"""
    Queries Reddit API for number of
    subscribers for a given subreddit
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


def number_of_subscribers(subreddit):
    """ query function """
    import requests
    headers = {
        'user-agent': get_user_agent()
    }
    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(
            subreddit),
        headers=headers
    )

    if response.status_code == 404:
        return 0

    json = response.json()
    data = json['data']
    return data["subscribers"]
