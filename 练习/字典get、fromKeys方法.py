#get方法在找不到key时不报错，并可以设置默认值，返回默认值

a = {"a":1,"b":2,"c":3}
print(a.get("b"))
print(a.get("d")) #不报错
print(a.get("d",100))


#fromKeys
t = (1,2,3)
a = dict.fromkeys(t,"hello")
print(a)
