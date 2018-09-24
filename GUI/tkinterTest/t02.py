import tkinter

def say(event):
    print("被点击了")

window = tkinter.Tk()

lb = tkinter.Label(window,text="按钮")
#绑定左键点击事件
lb.bind("<Button-1>",say)
lb.pack()
window.mainloop()