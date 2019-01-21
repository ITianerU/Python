
import json

str = """
    [{
        "name": "老王",
        "gender": "男",
        "birthday": "1995-8-9"
    },{
        "name": "老刘",
        "gender": "男",
        "birthday": "1996-10-11"
    }]
"""

data = json.loads(str)
print(data)

with open('data.json', 'w', encoding='utf-8') as f:
    # ensure_ascii使用中文编码, indent缩进
    f.write(json.dumps(data, ensure_ascii=False, indent=2))

with open('data.json') as f:
    print(json.loads(f.read()))
