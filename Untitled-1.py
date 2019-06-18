import requests
response = requests.get('http://www.baidu.com')
print(response)
print(response.headers)