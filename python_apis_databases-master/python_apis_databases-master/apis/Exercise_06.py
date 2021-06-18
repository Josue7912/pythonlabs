'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.

'''
import requests
from pprint import pprint

entryline = input(f'''
                    1) Create a new account (POST)
                    2) View all your tasks (GET)
                    3) View your completed tasks (GET)
                    4) View only your incomplete tasks (GET)
                    5) Create a new task (POST)
                    6) Update an existing task (PATCH/PUT)
                    7) Delete a task (DELETE)
Please input your option by writing the option number:  ''')


url = "http://demo.codingnomads.co:8081/tasks_api/users"

Email = input(f"Input your email address: " )

body = {
    "email": f"{Email}"
    }
response = requests.get(url, params=body)
data = response.json()
myid = data["data"][0]["id"]
pprint(f"Your user id is {myid}")


if entryline == "1":
    Name = input(f"Input your name: ")
    LastName = input(f"Input your last name: " )

    body = {
        "first_name": f"{Name}",
        "last_name": f"{LastName}",
        "email": f"{Email}"
    }
    response = requests.post(url, json=body)
    print(response.status_code)
    response = requests.get(url)
    data = response.json()
    pprint(data)

elif entryline == "2":
    task_url = "http://demo.codingnomads.co:8081/tasks_api/tasks/"
    params = {
        "userId" : myid,
        "complete" : "-1"
    }
    response = requests.get(task_url, params=params)
    data = response.json()
    pprint(data)