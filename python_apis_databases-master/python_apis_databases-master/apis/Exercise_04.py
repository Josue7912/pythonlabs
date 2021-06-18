'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 366,
    "first_name": "Jose",
    "last_name": "Perez",
    "email": "jose.perez.ferrera@hp.com"
}

response = requests.put(url, json=body)
print(response.status_code)

response = requests.get(url)
data = response.json()
pprint(data)