import xml.dom.minidom as xdm
from xml.dom.minidom import parse

#加载xml文件
DOMTree = xdm.parse("people.xml")
#得到文档对象
dom = DOMTree.documentElement
#读取子元素
for i in dom.childNodes:
    j = i.childNodes
    for m in j:
        if m.nodeName == "name":
            print(m.childNodes[0].data)
        if m.nodeName == "age":
            print(m.childNodes[0].data)