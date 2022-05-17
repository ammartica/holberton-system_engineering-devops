#!/usr/bin/python3
""" Script that, using a REST API for a given employee ID,
returns information about his/her TODO list progress """

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(user_id)).json()
    comp_tasks = []
    for task in todo:
        if task.get('completed') is True:
            comp_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(comp_tasks), len(todo)))
    for task in comp_tasks:
        print("\t {}".format(task))
