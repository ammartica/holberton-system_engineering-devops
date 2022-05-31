#!/usr/bin/python3
"""recursive method returns list of all hot article titles of given subreddit"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """returns list of titles of hot articles of a given subreddit"""
    headers = {'User-Agent': 'User Agent'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        nex = response.json().get('data').get('after')
        if nex is not None:
            after = nex
            recurse(subreddit, hot_list)
        titles = response.json().get('data').get('children')
        for title in titles:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return (None)
