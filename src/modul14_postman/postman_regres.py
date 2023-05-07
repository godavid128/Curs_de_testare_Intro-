import requests

url = "https://reqres.in/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# import requests
#
# url = "https://reqres.in/api/users?name=david&jog=DriverCar"
#
# payload={}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
