class A():
    def pset(self,name):
        print("被赋值了")
        self.name = name
    def pget(self):
        print("被获取了")
        return self.name
    def pdel(self):
        del self.name
        print("被删除了")
    name2 = property(pget,pset,pdel,"hahahahahaha")
a = A()
a.name2 = "老李"
print(a.name2)
del a.name2
print(a.name2)