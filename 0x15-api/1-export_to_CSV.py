#!/usr/bin/python3
""" script to export data in the CSV format """

import csv
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(emp_id)).json()
    with open("{}.csv".format(emp_id), 'w') as csvf:
        filler = csv.writer(csvf, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos:
            filler.writerow([emp_id, user.get('username'),
                            task.get('completed'), task.get('title')])
