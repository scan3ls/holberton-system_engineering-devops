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


def top_ten(subreddit):
    """ query function """
    import requests
    headers = {
        'user-agent': get_user_agent()
    }
    payload = {
        'limit': '10'
    }
    response = requests.get(
        'https://www.reddit.com/r/{}/top.json'.format(
            subreddit),
        headers=headers,
        params=payload
    )

    if response.status_code == 404:
        print(None)
        return

    json = response.json()
    posts = json['data']['children']
    
    for post in posts:
        data = post['data']
        title = data['title']
        print(title)