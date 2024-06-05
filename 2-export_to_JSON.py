#!/usr/bin/python3
import sys
import requests
import json

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()
    employee_name = todos[0]['name']

    tasks = []
    for todo in todos:
        task_info = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        }
        tasks.append(task_info)

    # Create JSON file
    with open(f"{employee_id}.json", 'w') as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
