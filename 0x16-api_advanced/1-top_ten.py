
#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit"""
    import requests
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
    else:
        for post in response.json().get('data').get('children'):
            print(post.get('data').get('title'))
