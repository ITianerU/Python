
import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient('mongodb://localhost:27017/')
# 指定数据库
db = client.test
# 指定表
collection = db.students

# student = {
#     'id': '20190101',
#     'name': '老王',
#     'age': 20,
#     'gender': 'male'
# }
# 插入,不推荐使用insert,请使用insert_one
# result = collection.insert(student)
# print(result)
# print('*'*100)
# student = {
#     'id': '20190107',
#     'name': 'marry',
#     'age': 20,
#     'gender': 'male'
# }
# result = collection.insert_one(student)
# print(result)

# 插入多条数据,不推荐使用insert,使用insert_many
# student1 = {
#     'id': '20190102',
#     'name': '老李',
#     'age': 22,
#     'gender': 'male'
# }
# student2 = {
#     'id': '20190103',
#     'name': '老刘',
#     'age': 22,
#     'gender': 'male'
# }
# result = collection.insert([student1, student2])
# print(result)
# student1 = {
#     'id': '20190105',
#     'name': '老李2',
#     'age': 22,
#     'gender': 'male'
# }
# student2 = {
#     'id': '20190106',
#     'name': '老刘2',
#     'age': 22,
#     'gender': 'male'
# }
# result = collection.insert([student1, student2])
# print(result)

# 查询
result = collection.find_one({'name': '老王'})
print(result)

# 通过objectid查询
result = collection.find_one({'_id': ObjectId('5c446e91eba7cb4b2acaaadf')})
print(result)
print('*'*100)

# 查询多条数据
results = collection.find({'age': 20})
for r in results:
    print(r)
print('*' * 100)

# 查询年龄大于20的数据, 小于lt,小于等于lte,大于gt,大于等于gte,不等于ne,在范围内in,不在范围内nin
results = collection.find({'age': {'$gt': 20}})
for r in results:
    print(r)
print('*'*100)

# 正则查询
results = collection.find({'name': {'$regex': '.*刘$'}})
for r in results:
    print(r)
print('*'*100)

# 判断属性是否存在, 为True时返回包含此字段的数据,为False时返回不包含此字段的数据
results = collection.find({'name': {'$exists': True}})
for r in results:
    print(r)
print('*'*100)

# 返回指定属性的类型为指定类型的数据
results = collection.find({'age': {'$type': 'int'}})
for r in results:
    print(r)
print('*'*100)

# 返回指定属性取模等于指定值的数据,如下,返回age%10=2的数据
results = collection.find({'age': {'$mod': [10, 2]}})
for r in results:
    print(r)
print('*'*100)

# 计数
count = collection.find().count()
print(count)
print('*'*100)

# 排序
results = collection.find().sort('id', pymongo.DESCENDING)
for result in results:
    print(result)
print('*'*100)

# 偏移,指查询出全部数据后,让指向第一行数据的指针,指向偏移数量之后的数据
results = collection.find().skip(4)
for result in results:
    print(result)
print('*'*100)

# limit,查询出全部数据后,返回的前N条数据
results = collection.find().limit(2)
for result in results:
    print(result)
print('*'*100)

# 修改
# student = {
#     'age': 25,
#     'gender': 'male'
# }
# result = collection.update_one({'name': 'tom'}, {'$set': student})
# print(result)
# 将年龄大于20的人,年龄加1,update_one只对匹配的第一个结果做操作
# result = collection.update_one({'age': {'$gt': 20}}, {'$inc': {'age':1}})
# print(result)
# result = collection.update_many({'age': {'$gt': 20}}, {'$inc': {'age':1}})
# print(result.matched_count)

# 删除
# result = collection.delete_one({'name': 'tom'})
# print(result)
# result = collection.delete_many({'name': 'tom'})
# print(result)
