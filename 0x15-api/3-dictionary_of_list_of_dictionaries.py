#!/usr/bin/python3
"""
    Script that uses a restful api and Records all tasks from all employees,
    returns information about his/her TODO list progress.
    and exports data in JSON format
"""
import json
import requests


def export_all_employees_todo():
    """Makes a GET request to the restful API endpoint"""
    # get employee name
    user_respons = requests.get('https://jsonplaceholder.typicode.com/users')
    users = user_respons.json()

    # get all employee data
    all_data = {}
    for user in users:
        employee_id = user['id']

        # Make a GET request to the API endpoint for each employee
        res = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(employee_id))
        todos = res.json()

        # exports data to json
        data = [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos
        ]

        all_data[employee_id] = data

    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(all_data, file)


if __name__ == '__main__':
    export_all_employees_todo()
