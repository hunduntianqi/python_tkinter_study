"""
    常用组件介绍:
        复选按钮 ==> Checkbutton
        单选按钮 ==> Radiobutton
        文本域 ==> Text
        画布 ==> Canvas
        创建新窗口 ==> Toplevel
"""
from tkinter import *


# 定义函数, 创建复选按钮
def creat_check_button():
    global main_window
    timeA = 0
    timeB = 0

    def funcA():
        nonlocal timeA, lab, lab_num
        if timeA % 2 == 0:
            timeA += 1
            lab["text"] = "Python学科被选中"
            lab_num["text"] = "timeA = {}".format(timeA)
        else:
            timeA += 1
            lab["text"] = "Python学科被取消"
            lab_num["text"] = "timeA = {}".format(timeA)

    def funcB():
        nonlocal timeB, lab, lab_num

        if timeB % 2 == 0:
            timeB += 1
            lab["text"] = "C++学科被选中"
            lab_num["text"] = "timeB = {}".format(timeB)
        else:
            timeB += 1
            lab["text"] = "C++学科被取消"
            lab_num["text"] = "timeB = {}".format(timeB)

    btnA = Checkbutton(main_window, text="Python学科", command=funcA)
    btnA.pack()
    btnB = Checkbutton(main_window, text="C++学科", command=funcB)
    btnB.pack()
    lab = Label(main_window, text=" ")
    lab_num = Label(main_window, text=" ")
    lab.pack()
    lab_num.pack()


# 定义函数, 创建单选按钮
def creat_radio_button():
    global main_window
    timeA = 0

    def funcA():
        nonlocal timeA, lab
        if timeA % 2 == 0:
            timeA += 1
            lab["text"] = "Python学科被选中"
        else:
            timeA += 1
            lab["text"] = "Python学科被取消"

    btnA = Radiobutton(main_window, text="Python学科", command=funcA)
    btnA.pack()
    lab = Label(main_window, text=" ")
    lab.pack()


# 定义函数, 创建一个文本域
def creat_text_area():
    global main_window
    # 创建一个文本域对象
    text = Text(main_window, width=50, height=30)
    text.pack()


# 定义函数, 创建新窗口
def creat_new_window():
    global main_window, WIDTH, HEIGHT, LEFT_SCREEN, TOP_SCREEN

    def new_window():
        top = Toplevel(main_window, width=300, height=200)
        top.title("我是toplevel窗⼝")
        top.geometry("{}x{}+{}+{}".format(WIDTH-100, HEIGHT-100, LEFT_SCREEN+50, TOP_SCREEN+50))
        lt = Label(top, text="我属于toplevel")
        lt.pack()

    button = Button(main_window, text="点我创建新窗口", command=new_window)
    button.pack()


if __name__ == '__main__':
    # 创建窗口对象
    main_window = Tk()
    # 修改窗口名
    main_window.title("组件测试窗口")
    # 定义窗口大小与位置
    WIDTH = 500
    HEIGHT = 400
    LEFT_SCREEN = 700
    TOP_SCREEN = 340
    main_window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, LEFT_SCREEN, TOP_SCREEN))
    creat_new_window()
    # 调用mainloop()方法
    main_window.mainloop()
