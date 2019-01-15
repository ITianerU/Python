
from bs4 import BeautifulSoup
import re

html = """
    <div class="panel">
        <div class="panel-heading>
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
"""

soup = BeautifulSoup(html, 'lxml')
# 输出节点为ul的全部节点
print(soup.find_all(name="ul"))
# 查出所有ul节点,再从每个ul节点中查询全部li子节点
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
# 查出所有ul节点,再从每个ul节点中查询全部li子节点,最后输出每个li的文本数据
for ul in soup.find_all(name='ul'):
    for li in ul.find_all(name='li'):
        print(li.string)
print("*" * 100)

html = """
    <div class="panel">
        <div class="panel-heading>
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
"""
soup = BeautifulSoup(html, 'lxml')
# 通过属性查询节点
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))
# 通过id,class查询节点
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))

print("*" * 100)

html = """
    <div class="panel">
        <div class="panel-body">
            <a>Hello, this is a link</a>
            <a>Hello, this is a link, too</a>
        </div>
    </div>
"""
soup = BeautifulSoup(html, 'lxml')
# 使用正则查找
print(soup.find_all(text=re.compile("link")))

"""
常用方法
查找第一个  find() 
查找父节点  find_parents() find_parent() 
查找兄弟节点  find_next_siblings() find_next_sibling() find_previous_siblings() find_previous_sibling()
查找前后节点  find_all_next() find_next() find_all_previous() find_previous()
"""