#!/usr/bin/python3
"""
   Script that uses a restful api for a given employee ID,
   returns information about his/her TODO list progress.
   and exports data in CSV format
"""
import csv
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
    employee_name = user['username']

    # exports data to csv
    filename = '{}.csv'.format(employee_id)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, employee_name,
                            task['completed'], task['title']])


    if __name__ == '__main__':
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
