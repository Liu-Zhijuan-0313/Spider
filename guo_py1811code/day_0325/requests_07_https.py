import requests
response = requests.get('https://kennethreitz.com', verify=True)
print(response.text)




