class A():
    name = "老李"
    age = 18
    def say(self):
        self.hight = 180
        __class__.sex = "男"
        print("我的身高是{0}，性别{1}".format(self.hight,__class__.sex))
a = A()
a.say()