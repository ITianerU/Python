class student():
    def say(self):
        print("我能说")

def sayHello():
    print("Hello")


#使用__name__ == "__main__",本文件自己运行时执行,被别的文件导入时不执行
if __name__ == "__main__":
    print("入口")
