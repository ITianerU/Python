#使用etree创建xml
import xml.etree.ElementTree as xee

toy = xee.Element("toy")
car = xee.Element("car")
# car = xee.SubElement(toy,"car")
car.attrib = {"height":"1.5","width":"3"}
car.text = "劳斯莱斯-魅影"
toy.append(car)

xee.dump(toy)

#创建xml文件
root = xee.ElementTree()
root._setroot(toy)
root.write("toy.xml")