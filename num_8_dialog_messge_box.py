"""
    对话框和消息框:
        创建对话框:
            dialog_object = Dialog(None, title="dialog_name", text=str, bitmap=dialog_type, default=0, strings=(str*))
                title ==> 对话框标题, 必须填
                text ==> 对话框中的提示内容, 必须填
                bitmap ==> 必须填, 一般为DIALOG_ICON
                strings ==> 指定对话框中的选项按钮, 可以指定多个
            其他对话框有:
                简单对话框 ==> simpledialog
                一般对话框 ==> commondialog
                文件对话框 ==> filedialog
        创建消息框:
           tkinter.messagebox.showinfo(title="传智播客Python学院", message="好好学习，天天向上！")
               title ==> 消息框标题
               message ==> 提示消息
"""
from tkinter import *
from tkinter import messagebox
from tkinter.dialog import *
from tkinter.dialog import DIALOG_ICON


# 定义函数, 创建对话框
def creat_dialog():
    global main_window

    def my_dialog():
        dialog_name = Dialog(None, title="Python调查", text="喜欢Python吗？", bitmap=DIALOG_ICON, default=0,
                             strings=("喜欢", "很喜欢", "⾮常喜欢"))
        print(dialog_name.num)

    btn_begin = Button(main_window, text="Python调查", command=my_dialog)
    btn_begin.pack()
    btn_quit = Button(main_window, text="关闭", command=btn_begin.quit)
    btn_quit.pack()


# 定义函数, 创建消息框
def creat_message_box():
    global main_window

    # 定义一个内函数, 用于绑定事件
    def my_messagebox():
        # 点击按钮后弹出一个提示框
        messagebox.showinfo(title="传智播客Python学院", message="好好学习，天天向上！")

    # 创建一个按钮组件
    button = Button(main_window, text="点击获取提示信息", command=my_messagebox)
    button.pack()


if __name__ == '__main__':
    main_window = Tk()
    # 定义窗口名称
    main_window.wm_title("创建菜单")
    # 定义窗口大小与位置
    width = 500
    height = 400
    left_screen = 700
    top_screen = 340
    main_window.geometry("{}x{}+{}+{}".format(width, height, left_screen, top_screen))
    # creat_dialog()
    creat_message_box()
    # 调用mainloop()方法
    main_window.mainloop()
    pass
