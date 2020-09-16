#!/usr/bin/python3
"""
    Retrieve information from an API
"""


def get_users_tasks(user_id=None):
    """
        get tasks by user
    """
    if user_id is None \
            or user_id == "":
        return tasks
    task_list = {}
    for task in tasks:
        if task['userId'] is not user_id:
            continue
        task_list[task['id']] = {
            'task': task['title'],
            'completed': task['completed']
        }
    return task_list


def all_json(users, tasks):
    """
        Compiles a json file of task
        info given

        Attributes:
            user - desired user
            tasks - list of tasks
    """
    import json

    if users is None or \
            tasks is None:
        return

    user_dict = {}
    for user in users:
        tasks = get_users_tasks(user['id'])
        task_list = []
        for task in tasks.values():
            task["username"] = user['username']
            task_list.append(task)
        user_dict[str(user['id'])] = task_list

    p = json.dumps(user_dict)
    with open("todo_all_employees.json", "w") as f:
        f.write(p)

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) != 1:
        print("Usage: ./0-gather_data_from_an_API <user_id>")
        exit()

    main_api = 'https://jsonplaceholder.typicode.com'
    if len(argv) == 2:
        user_id = int(argv[1])
    else:
        user_id = ""

    task_url = '{}/todos'.format(main_api)
    response = requests.get(task_url)
    tasks = response.json()

    user_url = '{}/users/{}'.format(main_api, user_id)
    response = requests.get(user_url)
    user = response.json()

    all_json(user, tasks)
