#!/usr/bin/python3
"""
Fetches data from JSONPlaceholder API for all users'
todo lists and exports to JSON
"""
import json
import requests

API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    users_response = requests.get(f"{API}/users")
    todos_response = requests.get(f"{API}/todos")

    users = users_response.json()
    todos = todos_response.json()

    all_users = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
            for todo in todos if todo.get("userId") == user_id
        ]

        all_users[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_users, json_file)
