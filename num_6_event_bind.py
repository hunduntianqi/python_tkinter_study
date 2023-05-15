"""
    事件绑定:
        bind(事件类型, 回调函数)函数:
            回调函数: 当事件发生后自动调用的绑定函数
            事件类型:
                1. <Button-1> 表示⿏标左键单击, 其中的 1 换成 3 表示右 键被单击, 为 2 的时候表示
                    ⿏标中键, 感觉不算常⽤
                2. <KeyPress-A> 表示 A 键被按下, 其中的 A 可以换成其他的键位
                3. <Control-V> 表示按下的是 Ctrl 和 V 键, V 可以换成其他 键位
                4. <F1> 表示按下的是 F1 键, 对于 Fn 系列的, 都可以随便换
        关于 bind 函数:
            bind_all()函数: 参数类型和 bind() 函数⼀样, 通常⽤于全局的快捷键
            bind_class("class-name", 事件类型, 回调函数)函数: 可以绑定某些类别
                例: w.bind_class(“Entry”, “<Control-V>”, my_paste) ==> 绑定了所有的所有的输⼊框的 Ctrl+V 表示粘贴
        解除绑定:
            unbind(事件类型): 会解除该绑定事件类型的所有回调函数
"""
from tkinter import *


def myLabel(event):
    global py
    s = Label(py, text="传智播客Python学院，好好学习天天向上！")
    s.pack()


if __name__ == '__main__':
    py = Tk()
    n = Label(py, text="我可不是真Button哟~")
    n.bind("<Button-1>", myLabel)
    n.pack()
    py.mainloop()
