import requests

url = "https://api.publicapis.org/entries"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# print(response.json())
# for k, v in response.json().items():
#     print(k, v)

# todo extrageti din intreg raspunsul doar acest link: 'https://yandex.com/dev/weather/'
#  request la link-urile 2 si 3:
# 1. https://api.publicapis.org/entries
# 2. https://datausa.io/api/data?drilldowns=Nation&measures=Population
# 3. https://reqres.in/