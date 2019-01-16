
from pyquery import PyQuery
import requests

html = """
    <div id="container">
        <ul>
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span>third item</span></a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
"""

result = PyQuery(html)
# class选择器
print(result('.item-0'))
# id选择器
print(result('#container'))

# find 查找所有子孙节点中匹配的节点,
print(result('#container').find('span'))
# children查找子节点匹配的节点
print(result('#container').children('ul'))
# parent 查找父节点
print(result('span').parent())
# parent 查找祖先节点
print(result('span').parents())
print("*"*100)
print(result('span').parents("ul"))
# siblings 查找兄弟节点
print(result('.active').siblings('li'))
# 遍历
for i in result('li').items():
    print(i)
# 获取属性
for i in result('a').items():
    print(i.attr('href'))
# 获取文本,无需遍历,获取的多个文本自动拼接成字符串,用空格连接
print(result('li').text())
print("*"*100)
# 获取HTML文本
for i in result('li').items():
    print(i.html())
# 删除,添加class
print(result('#container').add_class("container"))
print(result('#container').remove_class("container"))
# 修改属性,节点,文本
print(result("span").attr("height", "500px"))
print(result("span").text("老王"))
print(result("span").html("<b>老刘</b>"))
# 移除节点 类似方法还有 append(), empty(), prepend()
a = result("a[href='link3.html']")
print(a)
a.find("span").remove()
print(a)
print("*"*100)
# 伪类选择器
print(result("li:first"))
print(result("li:nth-child(2)"))
print(result("li:gt(2)"))
print(result("li:contains(fifth)"))
print(result("li:nth-child(2n)"))
