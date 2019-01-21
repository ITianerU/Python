
import pymysql

# db = pymysql.connect(host="localhost", user="root", password="123456", port=3306)
# cursor = db.cursor()
# cursor.execute('select version()')
# data = cursor.fetchone()
# print(data)
# 创建数据库
# cursor.execute("create database spiders default  character  set utf8")

# 创建表
# db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="spiders")
# cursor = db.cursor()
# sql = "create table if not exists students (id varchar (255) not null ,name varchar (255) not null ,age int not null ,primary key (id))"
# cursor.execute(sql)
# cursor.close()

# 插入
# id = "20190102"
# name = '老李'
# age = '46'
# db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="spiders")
# cursor = db.cursor()
# try:
#     cursor.execute('insert into students(id,name,age) values(%s, %s, %s)', (id, name, age))
#     db.commit()
# except:
#     db.rollback()
# cursor.close()

# 动态插入
# db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="spiders")
# data = {
#     'id': "20190102",
#     'name': '老王',
#     'age': '20'
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s']*len(data))
# sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
# cursor = db.cursor()
# try:
#     cursor.execute(sql, tuple(data.values()))
#     print('插入成功')
#     db.commit()
# except:
#     print('插入失败')
#     db.rollback()
# cursor.close()

# 修改
# name = '老刘'
# age = '99'
# db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="spiders")
# cursor = db.cursor()
# try:
#     cursor.execute('update students set age=%s where name=%s', (age, name))
#     print('编辑成功')
#     db.commit()
# except:
#     print('编辑失败')
#     db.rollback()
# cursor.close()

# 修改,判断主键是否存在,若存在则修改,不存在则插入
# db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="spiders")
# data = {
#     'id': "20190102",
#     'name': '老王',
#     'age': '50'
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s']*len(data))
# sql = 'insert into {table}({keys}) values ({values}) on duplicate key update'.format(table=table, keys=keys, values=values)
# update = ','.join([" {key} = %s".format(key=key) for key in data])
# sql += update
# cursor = db.cursor()
# try:
#     cursor.execute(sql, tuple(data.values())*2)
#     print('成功')
#     db.commit()
# except:
#     print('失败')
#     db.rollback()
# cursor.close()

# 删除
# db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="spiders")
# cursor = db.cursor()
# try:
#     cursor.execute('delete from students where age <= 50')
#     print('删除成功')
#     db.commit()
# except:
#     print('删除失败')
#     db.rollback()
# cursor.close()

# 查询
db = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="spiders")
cursor = db.cursor()
try:
    cursor.execute('select * from students')
    print(cursor.rowcount)
    # 返回指针指向的数据
    print(cursor.fetchone())
    # 返回指针指向的数据后后面的全部数据,当数据量大时不推荐用fetchall()
    print(cursor.fetchall())
    # 数据量大时,使用如下方法
    # data = cursor.fetchone()
    # while data:
    #     print(data)
    #     data = cursor.fetchone()
except:
    print('查询失败')
cursor.close()