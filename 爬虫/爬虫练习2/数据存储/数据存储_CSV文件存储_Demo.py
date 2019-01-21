
import csv

with open('data.csv', 'w') as f:
    # delimiter=' '以空格分割,默认为逗号分割
    c = csv.writer(f, delimiter=' ')
    c.writerow(['id', 'name', 'age'])
    c.writerow(['1', '老王', '20'])
    c.writerow(['2', '老刘', '22'])
    c.writerow(['3', '老毕', '21'])
    # 同时存入多条数据
    c.writerows([['4', '老大', '20'], ['5', '老二', '20'], ['6', '老三', '20']])

# 将字典格式数据写入csv文件
with open('data2.csv', 'w') as f:
    fieldnames = ['id', 'name', 'age']
    c = csv.DictWriter(f, fieldnames=fieldnames, delimiter=' ')
    c.writeheader()
    c.writerow({'id': '1', 'name': '老王', 'age': 20})
    c.writerow({'id': '2', 'name': '老李', 'age': 20})
    c.writerow({'id': '3', 'name': '老刘', 'age': 20})

# 读取csv文件
with open('data2.csv', 'r', encoding='utf-8') as f:
    c = csv.reader(f)
    for i in c:
        print(i)

# 使用pandas读取csv文件
import pandas
df = pandas.read_csv('data.csv')
print(df)





