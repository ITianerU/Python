import tkinter

def sayHello():
    print("hello")
#测试
#tkinter._test()

window = tkinter.Tk()
#设置标题
window.wm_title("标题")
#设置标题,目前没发现区别,百度也没查到
# window.title("标题2")

#label组件
label = tkinter.Label(window,text="label1",background="red")
button = tkinter.Button(window,text="button1",command=sayHello)
#布局
label.pack()
button.pack()

#消息循环
window.mainloop()


