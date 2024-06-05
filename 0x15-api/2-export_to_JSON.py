#!/usr/bin/python3
"""Export data from JSONPlaceholder API to JSON"""
import json
import requests
import sys

API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    USER_ID = sys.argv[1]
    url_to_user = f"{API}/users/{USER_ID}"
    url_to_task = f"{url_to_user}/todos"

    user_response = requests.get(url_to_user)
    todos_response = requests.get(url_to_task)

    user_data = user_response.json()
    todos_data = todos_response.json()

    USERNAME = user_data.get('username')
    dict_data = {USER_ID: []}

    for task in todos_data:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME
        })

    json_filename = f"{USER_ID}.json"
    with open(json_filename, 'w') as f:
        json.dump(dict_data, f)
