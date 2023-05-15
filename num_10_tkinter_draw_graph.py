"""
    tkinter_图形绘制组件 ==> Canvas:
        Canvas: 可以理解为画布, 用于绘制图形
        创建画布对象 ==> canvas_object= Canvas(window_object, width, height, bg="color")
                width ==> 画布宽度, 单位是像素
                height ==> 画布高度, 单位是像素
                bg ==> 画布背景颜色
        绘制线条 ==> canvas_object.create_line(start_coordinate, end_coordinate, width)
            start_coordinate ==> 线条起始坐标(x, y)
            end_coordinate ==> 线条末端坐标(x, y)
            width ==> 线条宽度
            注意: x / y是相对画布来说的, 画布区域左上角为 x=0, y=0
        绘制文字 ==> canvas_object.create_text(x, y, text=str)
"""
from tkinter import *


# 定义函数, 简单使用绘制组件
def simple_draw():
    global main_window
    canv = Canvas(main_window, width=500, height=400, bg="SkyBlue")
    canv.create_line((0, 0), (200, 200), width=8)
    canv.create_text(300, 30, text="Python学院")
    canv.pack()


# 定义函数, 绘制象棋棋盘
def draw_checkerboard():
    global main_window
    canv = Canvas(main_window, width=400, height=450)
    canv.create_line((0, 2), (400, 2), width=2)
    for i in range(10):
        canv.create_line((0, i * 50), (400, i * 50), width=2)
    canv.create_line((3, 0), (3, 450), width=2)
    for i in range(8):
        canv.create_line((i * 50, 0), (i * 50, 200), width=2)
    for i in range(8):
        canv.create_line((i * 50, 250), (i * 50, 450), width=2)
    canv.create_line((397, 0), (397, 450), width=2)
    canv.create_line((150, 0), (250, 100), width=2)
    canv.create_line((150, 100), (250, 0), width=2)
    canv.create_line((150, 450), (250, 350), width=2)
    canv.create_line((150, 350), (250, 450), width=2)
    canv.create_text(110, 220, text="汉界")
    canv.create_text(290, 220, text="楚河")
    canv.pack()


if __name__ == '__main__':
    # 创建窗口对象
    main_window = Tk()
    # 修改窗口名
    main_window.title("组件测试窗口")
    # 定义窗口大小与位置
    WIDTH = 400
    HEIGHT = 455
    LEFT_SCREEN = 700
    TOP_SCREEN = 340
    main_window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, LEFT_SCREEN, TOP_SCREEN))
    draw_checkerboard()
    # 调用mainloop()方法
    main_window.mainloop()
