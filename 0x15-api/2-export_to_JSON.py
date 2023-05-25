#!/usr/bin/python3
"""
    Script that uses a restful api for a given employee ID,
    returns information about his/her TODO list progress.
    and exports data in JSON format
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Makes a GET request to the restful API endpoint"""
    res = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(employee_id))
    todos = res.json()

    # filter completed task
    completed_tasks = [todo for todo in todos if todo['completed']]

    # get employee name
    user_respons = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(employee_id))
    user = user_respons.json()
    username = user['username']

    # exports data to json
    data = {employee_id: [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        for task in todos
    ]}
    filename = '{}.json'.format(employee_id)
    with open(filename, "w") as file:
        json.dump(data, file)


    if __name__ == '__main__':
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
