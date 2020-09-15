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
            'title': task['title'],
            'completed': task['completed']
        }
    return task_list


def get_completed_tasks(tasks={}):
    """
        get finished tasks by task set
    """
    if tasks == {}:
        return 0
    completed = 0
    task_list = []
    for task_id, task in tasks.items():
        if task['completed'] is False:
            continue
        completed += 1
        task_list.append(task['title'])
    return sorted(task_list), completed


def json_output(user=None, tasks=None):
    """
        Compiles a json file of task
        info given

        Attributes:
            user - desired user
            tasks - list of tasks
    """
    import json

    if user is None or \
            tasks is None:
        return

    user_id = str(user['id'])
    user_name = str(user['username'])
    tasks = get_users_tasks(int(user_id))
    file_name = "{}.json".format(user_id)
    with open(file_name, 'w') as f:
        list_of_tasks = []
        for task in tasks.values():
            list_of_tasks.append(
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": user_name
                }
            )
        p = json.dumps({user_id: list_of_tasks})
        f.write(p)

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) not in [1, 2]:
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

    json_output(user, tasks)
