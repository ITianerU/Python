
from bs4 import BeautifulSoup

html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class='title' name='dromouse'><b>The Dormouse's story</b></p>
            <p class='story'>Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.    
            </p>
            <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# 格式化输出
print(soup.prettify())
# 输出title
print(soup.title)
# 输出title的文本信息
print(soup.title.string)
print(soup.head)
print(soup.p)
# 输出节点名称
print(soup.p.name)
# 输出节点属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
# 获取子节点
print(soup.head.title)
print(soup.head.title.string)
# 输出节点内全部子节点内容,包括文本信息,节点等
print(soup.body.contents)
# 使用children输出节点内全部子节点内容,包括文本信息,节点等
for i, child in enumerate(soup.body.children):
    print(i, ' ', child)

# 输出节点内全部子孙节点内容,包括文本信息,节点等
for i, child in enumerate(soup.body.descendants):
    print(i, ' ', child)
# 输出父节点
print(soup.title.parent)
# 输出所有祖先节点
for i, parent in enumerate(soup.title.parents):
    print(i, '=', parent)
print("***"*30)
# 输出后面的兄弟节点,可能为文本,空格,节点
print(soup.a.next_sibling)
# 输出前面的兄弟节点,可能为文本,空格,节点
print(soup.a.previous_sibling)
# 输出后面的全部兄弟节点,包括文本,空格,节点
for i, sibling in enumerate(soup.a.next_siblings):
    print(i, '==', sibling)
# 输出前面的全部兄弟节点,包括文本,空格,节点
for i, sibling in enumerate(soup.a.previous_siblings):
    print(i, '==', sibling)






