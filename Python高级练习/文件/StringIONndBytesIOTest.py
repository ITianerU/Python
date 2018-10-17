#在内存中读写
from io import StringIO

f = StringIO()
f.write("hello")
f.write(" ")
f.write("everybody")
print(f.getvalue())

#操作二进制
from io import BytesIO

f = BytesIO()
f.write("老王".encode("utf-8"))
print(f.getvalue())
print(f.getvalue().decode("utf-8"))

import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
s2 = json.loads(s)
print(s2)