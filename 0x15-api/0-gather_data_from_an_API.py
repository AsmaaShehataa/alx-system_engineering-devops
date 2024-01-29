
#!/usr/bin/python3
"""Given Employee information, return their todo list progress."""

if __name__ == "__main__":
    import requests
    import sys
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    USER_ID = sys.argv[1]

    user_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{USER_ID}').json()
    USERNAME = user_info.get("username")

    _request = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={USER_ID}').json()

    for _task in _request:
        if _task.get('completed') is True:
            TASK_TITLE.append(_task.get('title'))
            NUMBER_OF_DONE_TASKS += 1

    TOTAL_NUMBER_OF_TASKS = len(_request)

    print('Employee {} is done with tasks({}/{}):'.
          format(USERNAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for title in TASK_TITLE:
        print('\t {}'.format(title))
