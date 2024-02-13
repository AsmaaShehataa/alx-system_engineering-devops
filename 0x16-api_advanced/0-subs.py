#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit API"""

import requests


def number_of_subscribers(subreddit):
    """ function to fetch number of subscribers """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-agent": "nadduli daniel"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return (data['data']['subscribers'])
    else:
        return 0
