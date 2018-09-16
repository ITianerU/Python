import json

person = {
    "name":"laowang",
    "age":23
}
#将字典转换为json
per_json = json.dumps(person)
print(type(per_json))
#将json转换为字典
per_dict = json.loads(per_json)
print(type(per_dict))

#将json写入
with open("person.json","w") as f:
    json.dump(per_dict,f)

#读取json文件
with open("person.json","r") as f:
    jsonf = json.load(f)
    print(jsonf)

