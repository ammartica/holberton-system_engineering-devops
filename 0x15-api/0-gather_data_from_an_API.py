#!/usr/bin/python3
""" Script that, using a REST API for a given employee ID,
returns information about his/her TODO list progress """

import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_id, verify=False)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(emp_id, verify=False)).json()
    name = user.get('name')
    comp_tasks = []

    for task in todos:
        if task.get('completed') is True:
            comp_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(comp_tasks), len(todos)))

    for task in comp_tasks:
        print("\t {}".format(task))
