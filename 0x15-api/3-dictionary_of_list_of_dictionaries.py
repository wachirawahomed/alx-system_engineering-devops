#!/usr/bin/python3
"""
Script to fetch tasks for all users and export them to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    # Fetch tasks for all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    tasks_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        users_response = requests.get(users_url)
        tasks_response = requests.get(tasks_url)

        users_data = users_response.json()
        tasks_data = tasks_response.json()

        # Organize tasks by user ID
        tasks_by_user = {}
        for task in tasks_data:
            user_id = task["userId"]
            task_entry = {
                    "username": "",
                    "task": task["title"],
                    "completed": task["completed"]
                    }
            # Find username corresponding to user ID
            for user in users_data:
                if user["id"] == user_id:
                    task_entry["username"] = user["username"]
                    break
            # Append task entry to user's list of tasks
            if user_id in tasks_by_user:
                tasks_by_user[user_id].append(task_entry)
            else:
                tasks_by_user[user_id] = [task_entry]

        # Export data to JSON format
        with open("todo_all_employees.json", "w") as json_file:
            json.dump(tasks_by_user, json_file)

        print("Data exported to todo_all_employees.json")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
