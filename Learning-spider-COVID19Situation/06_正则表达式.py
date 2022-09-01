import re

rs = re.findall('\d','123')
rs = re.findall('\d*','456')
rs = re.findall('\d+','789')
rs = re.findall('a+','aaabcd')

print(rs)
