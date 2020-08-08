import json

json_str = '''[
  {
    "a": "this is a",
    "b": [1, 2,"熊猫"]
  },
  {
    "c": "thia is c"
  }
]'''

rs = json.loads(json_str)
json_str = json.dumps(rs, ensure_ascii=False)
print(json_str)

with open("data/test1.json", 'w', encoding='utf8') as fp:
    json.dump(rs, fp, ensure_ascii=False)
