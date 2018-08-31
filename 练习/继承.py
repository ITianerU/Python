class People():
    __name = "老铁"
    _age = 18
    def say(self):
        print("hello~")

class LaoWang(People):
    def eat(self):
        super().say()
        print("我先吃了")

laoWang = LaoWang()

laoWang.eat()
print(People._age)

#子类继承的父类属性是同一地址
print(id(laoWang._age))
print(id(People._age))
