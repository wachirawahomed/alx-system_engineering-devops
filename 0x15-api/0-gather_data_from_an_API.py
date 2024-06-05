#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
"""
import requests
import sys

API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user = requests.get("{}/users/{}".format(API, employee_id)).json()
    todos = requests.get(
            "{}/todos".format(API),
            params={"userId": employee_id}
            ).json()
    completed_tasks = [
            task.get("title") for task in todos if task.get("completed")
            ]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)))
    [print("\t {}".format(task)) for task in completed_tasks]
