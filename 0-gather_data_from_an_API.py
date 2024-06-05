#!/usr/bin/python3
import sys
import requests

def get_employee_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    # Calculate progress
    total_tasks = len(todos)
    done_tasks = sum(1 for todo in todos if todo['completed'])

    # Display progress
    print(f"Employee {todos[0]['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)`
