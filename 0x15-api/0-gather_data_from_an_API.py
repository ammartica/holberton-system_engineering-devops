#!/usr/bin/python3
""" Script that, using a REST API for a given employee ID,
returns information about his/her TODO list progress """

import requests
from sys import argv


if __name__ == '__main__':
    argc = len(argv)
    if (argc == 2 and argv[1].isdigit()):

        REST = 'https://jsonplaceholder.typicode.com/'
        emp_id = argv[1]

        emp_response = requests.get(REST + 'users/' + emp_id)

        emp_name = emp_response.json().get("name")

        todo_response = requests.get(REST + 'todos?userId=' + emp_id)
        tasks = todo_response.json()

        tasks_done = 0
        task_count = 0
        task_string = ""

        for task in tasks:
            if task.get('completed') is True:
                tasks_done += 1
                task_string += "\t " + task.get('title') + '\n'
            task_count += 1
        print("Employee {} is done with tasks({}/{}):"
              .format(emp_name, tasks_done, task_count))
        print(task_string, end="")
