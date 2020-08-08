import re
import requests
from bs4 import BeautifulSoup


response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()

soup = BeautifulSoup(home_page,'lxml')
script = soup.find(id='getListByCountryTypeService2true')
text = script.string
# print(text)

json_str = re.findall(r'\[.+\]',text)[0]
print(json_str)
