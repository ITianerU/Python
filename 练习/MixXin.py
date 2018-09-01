class Eat():
    def eat(self):
        print("I can eat")
class Run():
    def run(self):
        print("I can run")
class People(Eat,Run):
    pass

laoWang = People()
laoWang.eat()
laoWang.run()
