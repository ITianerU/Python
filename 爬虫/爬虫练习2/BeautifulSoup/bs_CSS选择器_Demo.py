
from bs4 import BeautifulSoup

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
# 使用css选择器获取节点
print(soup.select(".element"))
print(soup.select("#list-1"))

# 获取节点的属性值
print(soup.select('#list-2')[0]['class'])
# 输出节点文本
print(soup.select('#list-1 li')[0].get_text())
