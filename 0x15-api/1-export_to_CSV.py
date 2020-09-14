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


def text_output(user, tasks):
    """
        Produces text output of task
        info given

        Attributes:
            user - desired user
            tasks - list of tasks
    """
    if user is None or tasks is None:
        return

    user_id = user['id']
    tasks = get_users_tasks(user_id)
    name = user['name']
    total_tasks = len(tasks)
    completed_tasks, completed = get_completed_tasks(tasks)

    msg = "Employee {} is done with tasks({}/{}):".format(
            name, completed, total_tasks
    )
    print(msg)
    for task in completed_tasks:
        print("\t", task)


def csv_ouput(user=None, tasks=None):
    """
        Compiles a csv file of task
        info given

        Attributes:
            user - desired user
            tasks - list of tasks
    """

    user_id = str(user['id'])
    tasks = get_users_tasks(int(user_id))
    file_name = "{}.csv".format(user_id)
    f = open(file_name, "w")
    for task in tasks.values():
        user_name = str(user['username'])
        task_status = str(task['completed'])
        task_title = str(task['title'])
        params = [user_id, user_name, task_status, task_title]
        entry = ','.join(map(lambda x: '"' + x + '"', params))
        f.write(entry + "\n")
    f.close()


def json_output(user=None, tasks=None, f=None):
    """
        Compiles a json file of task
        info given

        Attributes:
            user - desired user
            tasks - list of tasks
    """
    if user is None or \
            tasks is None or \
            f is None:
        return

    user_id = str(user['id'])
    user_name = str(user['username'])
    tasks = get_users_tasks(int(user_id))
    file_name = "{}.json".format(user_id)
    open_string = "\"{}\": [".format(user_id)
    f.write(open_string)
    counter = 0

    for task in tasks.values():
        title = task['title']
        status = str(task['completed']).lower()
        task_string = "{{\"task\": \"{}\", ".format(title)
        status_string = "\"completed\": {}, ".format(status)
        user_string = "\"username\": \"{}\"}}".format(user_name)
        string = task_string + status_string + user_string
        if counter == 0:
            f.write(string)
            counter = 1
        else:
            f.write(", " + string)

    close_string = "]"
    f.write(close_string)


def all_json(users, tasks):
    """
        Compiles a json file of task
        info given

        Attributes:
            user - desired user
            tasks - list of tasks
    """
    if type(users) is list:
        file_name = "todo_all_employees.json"
    else:
        file_name = "{}.json".format(users['id'])

    f = open(file_name, "w")
    f.write("{")
    if type(users) is list:
        for user in users:
            json_output(user, tasks, f)
            f.write(", ")
    else:
        json_output(users, tasks, f)

    f.write("}")
    f.close()

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

    # text_output(user, tasks)
    csv_ouput(user, tasks)
    # json_output(user, tasks)
    # all_json(user, tasks)
