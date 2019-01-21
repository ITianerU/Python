
from redis import StrictRedis

# host='localhost', port=6379, db=0为默认值,可省略
redis = StrictRedis(host='localhost', port=6379, db=0, password='123456')
# redis.set('name', '老王')
# print(redis.get('name').decode('utf8'))

# 键操作
# 判断键是否存在, 返回1表示存在,0表示不存在
print(redis.exists('name'))

# 删除键,返回1表示删除成功,0表示不不成功
# print(redis.delete('name'))

# 判断键的类型
print(redis.type('name'))

# 获取所有符合规则的键
print(redis.keys('n*'))

# 随机获取一个键
print(redis.randomkey())

# 重命名键,返回true表示修改成功
# print(redis.rename('name2', 'name'))

# 获取键的数量
print(redis.dbsize())

# 设定键的过期时间
# print(redis.expire('name', 10000))

# 获取键过期时间 -1为永久
print(redis.ttl('name'))

# 将键移动到其他数据库
# redis.move('name',其他数据库)

# 删除当前数据库所有键
# redis.flushdb()

# 删除所有数据库所有键
# redis.flushall()

# ===========================================================================================

# 字符串操作
# 给键赋值,取值
# redis.set('name', '老李')
print(redis.get('name'))

# 给键赋值,并返回旧值
# print(redis.getset('name', '老刘').decode())

# 返回多个键的值组成的列表
# redis.set('age', 20)
print(redis.mget(['name', 'age']))
# 批量赋值
# redid.mset({'name1': '小姜', 'name2': '老田'})

# 若键不存在,则创建新的键值对,不修改已存在的键值对,批量使用用msetnx
redis.setnx('age', 22)
print(redis.get('age'))
redis.setnx('id', 1)
print(redis.get('id'))
# redis.msetnx({'age1': 20, 'age2':30})

# 设置键值对,并设置过期时间
# redis.setex('time', 1, 1)

# 对值进行指定位置覆盖操作
# redis.setrange('name', 3, 'haha')
print(redis.get('name'))


