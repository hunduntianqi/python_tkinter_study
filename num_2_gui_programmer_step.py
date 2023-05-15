"""
    GUI编程步骤:
        1. 创建应用程序主窗口对象(根窗口)
        2. 在主窗口中添加各种可视化组件, 如: 按钮(Button), 文本框(Label)等
        3. 通过几何布局管理器, 管理组件的大小和位置
        4. 事件处理 ==> 通过绑定事件处理程序, 响应用户操作所触发的事件
"""
from tkinter import *
from tkinter import messagebox


# 定义函数, 监听并处理事件
def song_hua(event_song_hua: Event):
    messagebox.showinfo("Message", "送你一朵玫瑰花")
    pass


if __name__ == '__main__':
    """ GUI编程示例 """
    # 创建一个主窗口对象
    main_windows = Tk()
    # 定义窗口名称
    main_windows.title("我的第一个GUI编程界面")
    # 定义窗口大小与窗口位置
    main_windows.geometry("300x200+810+440")
    # 定义一个按钮组件并绑定窗口对象
    button = Button(main_windows)
    button['text'] = "点我就送一朵小红花~~"
    # 调用布局管理器, 将组件对象放入主窗口对象中
    button.pack()
    # 组件绑定事件, <Button-1> ==> 代表鼠标左键点击事件
    button.bind("<Button-1>", song_hua)
    main_windows.mainloop()  # mainloop() ==> 进入事件循环, 保证窗口存在
    pass
