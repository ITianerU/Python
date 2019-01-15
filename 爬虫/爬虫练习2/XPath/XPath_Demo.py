
from lxml import etree

text = """
    <div>
        <ul>
            <li class='item-0'><a href="link1.html">first item</a></li>
            <li class='item-1'><a href="link2.html">second item</a></li>
            <li class='item-inactive'><a href="link3.html">third item</a></li>
            <li class='item-1'><a href="link4.html">fourth item</a></li>
            <li class='item-0'><a href="link5.html">fifth item</a>
        </ul>
    </div>
"""

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode("utf-8"))

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

# 选取所有节点,返回一个列表
result = html.xpath("//*")
print(result)

# 选取指定节点,返回一个列表
result = html.xpath("//li")
print(result)

# 选取子节点,返回一个列表
result = html.xpath("//li/a")
print(result)

# 选取父节点属性,返回一个列表
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

# 选取父节点属性,返回一个列表
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

# 获取文本,返回一个列表
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

# 属性存在多个值时,用contains进行匹配
text = """
    <li class="li li-first" name="item"><a href="index.html">first item</a></li>
"""
html = etree.HTML(text)
result = html.xpath("//li[contains(@class, 'li')]/a/text()")
print(result)

# 同时匹配多个属性,用and连接
result = html.xpath("//li[contains(@class, 'li') and @name='item']/a/text()")
print(result)

# 选取同一级别节点的部分节点
text = """
    <div>
        <ul>
            <li class='item-0'><a href="link1.html">first item</a></li>
            <li class='item-1'><a href="link2.html">second item</a></li>
            <li class='item-inactive'><a href="link3.html">third item</a></li>
            <li class='item-1'><a href="link4.html">fourth item</a></li>
            <li class='item-0'><a href="link5.html">fifth item</a>
        </ul>
    </div>
"""
html = etree.HTML(text)
result = html.xpath("//li[1]/a/text()")
print(result)
result = html.xpath("//li[@class='item-0'][2]/a/text()")
print(result)
result = html.xpath("//li[last()]/a/text()")
print(result)
result = html.xpath("//li[position()<4]/a/text()")
print(result)


# 节点轴选择
# 所有祖先节点
print(html.xpath("//li[1]/ancestor::*"))
# 所有是div的祖先节点
print(html.xpath("//li[1]/ancestor::div"))
# 所有属性
print(html.xpath("//li[1]/attribute::*"))
# 所有子节点
print(html.xpath("//li[1]/child::a[@href='link1.html']"))
# 所有子孙节点
print(html.xpath("//li[1]/descendant::span"))
# 当前节点之后的左右节点,包括兄弟节点,子孙节点
print(html.xpath("//li[1]/following::*/text()"))
# 所有同级后续节点
print(html.xpath("//li[1]/following-sibling::*/a/text()"))




