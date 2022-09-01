import re

# 分组的使用
rs = re.findall('\d{1,2}','chuan13zhi2')
rs = re.findall('aaa(\d+)b','aaa91b')
print(rs)

# 一般的正则表达式匹配一个\需要四个\
rs = re.findall('a\\\\bc','a\\bc')
print(rs)
print('a\\bc')

# 使用r原串
rs = re.findall(r'a\\rbc','a\\rbc')
print(rs)

