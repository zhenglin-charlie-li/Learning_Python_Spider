import requests

response = requests.get('https://file1.dxycdn.com/2020/0315/553/3402160512808052518-135.json')
print(response.content.decode())