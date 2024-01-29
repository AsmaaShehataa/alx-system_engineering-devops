#!/usr/bin/python3

"""JSON file parser for the 'json' file."""

if __name__ == '__main__':
    import json
    import requests

    all_users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = all_users.json()

    all_tasks = {}

    for user in users:
        USER_ID = user["id"]
        req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                           format(USER_ID))
        todos = req.json()

        tasks = []
        for todo in todos:
            task = {
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            }
            tasks.append(task)

        all_tasks[USER_ID] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=2)
