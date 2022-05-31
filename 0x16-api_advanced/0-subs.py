#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of
subscribers for a given subreddit"""
import json
import requests


def number_of_subscribers(subreddit):
    """returns total number of subscribers per given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "User Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
