import requests
from bs4 import BeautifulSoup

url = 'http://jwc.scu.edu.cn/'
response = requests.get(url)
page = response.content.decode()
# print(page)
result = ''

soup = BeautifulSoup(page, 'lxml')
tag = soup.find_all(class_='list-llb-text')
# print(tag)
for each in tag:
    text = each.text
    # print(text)
    result += text

print(result)

with open('data.txt', 'w', encoding='utf8') as fp:
    for each in tag:
        text = each.text
        fp.write(text)
