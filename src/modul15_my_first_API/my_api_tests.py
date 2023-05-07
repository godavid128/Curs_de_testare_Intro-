import requests

# url = "http://localhost:8000/users"
#
# payload = "{\r\n    \"name\": \"andreea\",\r\n    \"email\": \"ab@gmail.com\",\r\n    \"salary\": 3000\r\n}"
# headers = {
#   'Content-Type': 'text/plain'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

import requests
import json


def post_request(name, email, salary):
    url = "http://localhost:8000/users"

    payload = json.dumps({
        "name": name,
        "email": email,
        "salary": salary
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.status_code


with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)
    for i in data:
        post_request(i['name'], i['email'], i['salary'])
        post_request('maria', 'm@gmail.com', 2000)
