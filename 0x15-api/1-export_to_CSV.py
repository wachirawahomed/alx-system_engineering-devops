#!/usr/bin/python3
""" Export data from JSONPlaceholder API to CSV """
import csv
import requests
import sys

API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    user_url = f"{API}/users/{user_id}"
    todos_url = f"{user_url}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data.get('username')
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                user_id,
                username,
                task.get('completed'),
                task.get('title')
                ])
