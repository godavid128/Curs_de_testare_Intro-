import requests

url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
