import requests

response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")

response.encoding=response.apparent_encoding
#print(response.text)
print(response.content.decode())
