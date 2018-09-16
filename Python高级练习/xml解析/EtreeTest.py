import xml.etree.ElementTree as xee

root = xee.parse("people.xml")
#获取所有子孙后代节点
nodes = root.getiterator()
for node in nodes:
    print(node.tag,"=",node.text)
print("*"*20)
#获取查询到的第一个节点
ele_person = root.find("person")
for node in ele_person:
    print(node.tag,"=",node.text)
print("*"*20)
#获取查询到的所有节点
ele_persons = root.findall("person")
for node in ele_persons:
    for i in node:
        print(i.tag, "=", i.text)
print("*" * 20)
#获取根节点的直接子节点
root2 = root.getroot()
for node in root2:
    print(node.tag,"=",node.text)

#iter筛选出指定名称的节点
for node in root2.iter("person"):
    if node.find("name") != None:
        #设置属性
        node.set("name",node.find("name").text+"~~")
        #操作元素的值text
        node.find("name").text += "~~"

dog = root.find("dog")
ele = xee.Element("age")
ele.attrib = {"age":"3"}
ele.text = "3"
dog.append(ele)

root.write("people.xml")

