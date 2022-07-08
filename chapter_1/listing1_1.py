import requests

response = requests.get('https://www.example.com')

items = response.headers.items()

headers = [f'{key}: {headers}' for key,headers in items]

formated_headers = '\n'.join(headers)

with open('../headers.txt', 'w+') as file:
    file.write(formated_headers)