"""
    tkinter_创建主窗口对象:
        a. 导入模块 ==> from tinker import *
        b. 创建主窗口 ==> main_window_object = Tk()
            注意: 在程序末尾必须使用 main_window_object 调用 mainloop() 方法, 来保证窗口一直存在
        c. 修改窗口名称 ==> main_window_object.title("window_name") 或者 main_window_object.wm_title("window_name")
        d. 定义窗口大小与窗口位置 ==> main_window_object.geometry("widthxheight±screen_width±screen_height")
            width ==> 窗口宽度, 单位是像素
            height ==> 窗口高度, 单位是像素
            screen_width ==> 距屏幕左右边的距离, '+'代表距离屏幕左侧, '-'代表距离屏幕右侧, 单位是像素
            screen_height ==> 距屏幕上下边的距离, '+'代表距离屏幕上侧, '-'代表距离屏幕下侧, 单位是像素
            注意: 四个属性参数之间不能有空格!!
        e: 去除边框 ==> main_window_object.overrideredirect(True)
        f: 修改标题栏默认图标 ==> main_window.iconbitmap("ico_file_name") 或 main_window.wm_iconbitmap("ico_file_name")
"""
from tkinter import *

if __name__ == '__main__':
    """ 创建一个窗口对象 """
    main_window = Tk()
    # 定义窗口名称
    main_window.wm_title("这是一个测试程序")
    # 定义窗口大小与位置
    WIDTH = 500
    HEIGHT = 400
    LEFT_SCREEN = 700
    TOP_SCREEN = 340
    main_window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, LEFT_SCREEN, TOP_SCREEN))
    # 去除边框
    # main_window.overrideredirect(True)
    # 修改标题栏默认图标
    # main_window.iconbitmap('img.ico')
    # 调用 mainloop() 方法
    main_window.mainloop()
