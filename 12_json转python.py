import json

# json字符串转python数据
json_str = '''[
  {
    "a": "thia is a",
    "b": [1, 2, 3]
  },
  {
    "c": "thia is c",
    "d": [1, 2, 3]
  }
]'''

rs = json.loads(json_str)
print(rs)
print(type(rs))  # <class 'list'>
print(type(rs[0]))  # <class 'dict'>
print(type(json_str))  # <class 'str'>

# json格式文件转python数据
with open('data/test.json') as fp:
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))  # <class 'list'>
    print(type(python_list[0]))  # <class 'dict'>
    print(type(fp))  # <class '_io.TextIOWrapper'>
