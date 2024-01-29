#!/usr/bin/python3

"""JSON file parser for the 'json' file."""

if __name__ == '__main__':
    import json
    import requests
    import sys

    USER_ID = sys.argv[1]
    _user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(USER_ID))
    user = _user.json()

    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(USER_ID))
    todos = req.json()

    tasks = []
    for todo in todos:
        task = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"]
        }
        tasks.append(task)

    with open(USER_ID + '.json', 'w') as json_file:
        json.dump({USER_ID: tasks}, json_file)
