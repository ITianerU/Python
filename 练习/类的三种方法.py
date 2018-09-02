class people():
    #类实例方法
    def say(self):
        print("我能说!")
    #类方法
    @classmethod
    def run(cls):
        print("我能跑!")
    #静态方法
    @staticmethod
    def eat():
        print("我能吃!")

one = people()
one.say()
one.eat()
one.run()
people.run()
people.eat()
