
from urllib import parse, request

# 解析url
result = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)

# 解析url 设置默认协议
result = parse.urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='http')
print(result)

result = parse.urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)

# 解析url 忽略fragment
result = parse.urlparse('www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
print(result)

# 构造url   urlunparse参数的长度必须是6，urlunsplit参数的长度必须是5
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(parse.urlunparse(data))

data = ['http', 'www.baidu.com', 'index.html;user', 'a=6', 'comment']
print(parse.urlunsplit(data))

# 将url1的scheme，netloc，path拼接到url2上
print(parse.urljoin('http://www.baidu.com/index.html', 'FAQ.html'))

# 序列化参数，拼接url用于get方法传值
params = {
    'name': 'germey',
    'age': 22
}
print('http://www.baidu.com?'+parse.urlencode(params))

# 反序列化
print(parse.parse_qs('name=germey&age=22'))

# 反序列化为元祖组成的列表
print(parse.parse_qsl('name=germey&age=22'))

# 将url中的中文字符转换为url编码
print('http://www.baidu.com/s?wd=' + parse.quote('熊猫'))

# 解码经url编码的中文字符
print(parse.unquote('http://www.baidu.com/s?wd=%E7%86%8A%E7%8C%AB'))


