#!/usr/bin/python3
""" Script that takes emp ID as input and
uses JSONPlaceholder API to get information about
employee then writes the info on a dictionary
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    json_o = res.json()
    d_task = {}
    for user in json_o:
        emp_name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        tasks = res.json()
        task_info = []
        for task in tasks:
            dict_task = {"username": emp_name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            task_info.append(dict_task)

        d_task[str(userid)] = task_info
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
