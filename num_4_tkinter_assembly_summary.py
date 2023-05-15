"""
    tkinter_组件简介:
        核心组件:
            在 Python 的 tkinter 中, 有 21 个核⼼组件, 它们提供了最基本的功能, 虽然简单, 因为使⽤频率较⾼, 因此特别重要
            21个核心组件为:
                Toplevel、Label、Button、 Canvas、Checkbutton、Entry、Frame、LabelFrame、
                Listbox、Menu、Menubutton、Message、OptionMenu、PaneWindow 、 Radiobutton 、
                Scale 、Scrollbar 、Spinbox 、Text、Bitmap、Image
        组件的使用:
            1. 每个组件都有相对应的类, 可以创建对应组件的对象使用
            2. 这些组件的使⽤也很相似, 在实例化这些组件的时候, 第⼀个参数都是⽗窗⼝或者⽗组件, 后⾯跟着的就是该组件的⼀些属性
            3. 多个组件的位置控制⽅式也很相似, 可以⽤ pack ⽅法来进⾏简单的布局
            4. 组件也会有些⽅法是共⽤的, ⽐如 configure ⽅法来设置属性等
        标签 ==> Label类:
            用于说明一些文字信息, 可以说是最简单的窗口组件了, 不需要执行任何功能, 只是用来显示信息
            创建一个标签对象:
                label_object = Label(window_object, text = message)
                    window_object ==> 要绑定标签的窗口对象
                    text ==> 要展示的信息内容
                    除此之外, Label对象还有background, font, bitmap, padx, relief, underline 等等属性
        按钮 ==> Button类:
            按钮是非常重要的组件, 按钮组件可以绑定函数执行相应的功能
            创建按钮对象: button_object = Button(window_object, text="button_message")
            设置按钮属性 ==> button_object["property_name"] = property_value
            按钮绑定函数:
                方式一: 定义按钮时, 通过按钮的 command 属性去绑定对应函数
                    例: button_object = Button(window_object, text="button_message", command=func_name)
                    则点击按钮时会执行绑定的函数
                方式二: 通过 bind() 方法绑定函数
                    例:
                        button_object = Button(window_object, text="button_message")
                        button_object.bind(("event_name", func_name)
                            event_name: 指要绑定的事件类型, 采⽤的描述⽅式是 <MODIFIER-MODIFIER-TYPE-DETAIL>
                                MODIFIER ==> 键盘或者鼠标修饰符, 全部取值如下:
                                    Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4, Button1, B1, Mod5, M5,
                                    Button2, B2, Meta, M, Button3, B3, Alt, Button4, B4, Double, Button5, B5 Triple,
                                    Mod1, M1
                                TYPE ==> 类型, 全部取值如下:
                                    Activate, Enter, Map, ButtonPress, Button, Expose, Motion, ButtonRelease, FocusIn,
                                    MouseWheel, Circulate, FocusOut, Property, Colormap, Gravity Reparent, Configure,
                                    KeyPress, Key, Unmap, Deactivate, KeyRelease Visibility, Destroy, Leave
                                DETAIL ==> 表示细节, 是对类型的一些说明
                            func_name: 执行功能的函数, 该函数必须包含一个形参代表监听的事件, 通常用 event 来表示
        输入框 ==> Entry类:
            应⽤程序要取得⽤户的信息, 输⼊框是必不可少的
            创建输入框对象:
                entry_object = Entry(window_object)
            获取输入框内容:
                message = entry_object.get()
            清空输入框内容:
                entry_object.delete(0, len(entry_object.get()))
            密码框:
                和输入框基本一样, 只需要设置输入框属性 entry_object['show'] = '*' 即可

"""
from tkinter import *


# Button绑定函数方式一测试函数
def button_test():
    # 声明全局变量
    global main_window, num_count
    # 创建一个标签组件对象
    label = Label(main_window, text="轻松愉快, 就选Python! 重要的事情说 {} 遍！".format(num_count), background="SkyBlue")
    # 标签组件放进绑定的窗口
    label.pack()
    num_count += 1


# Button绑定函数方式二测试函数
def button_test2(event: Event):
    # 声明全局变量
    global main_window, num_count
    # 创建一个标签组件对象
    label = Label(main_window, text="轻松愉快, 就选Python! 重要的事情说 {} 遍！".format(num_count), background="SkyBlue")
    # 标签组件放进绑定的窗口
    label.pack()
    num_count += 1


# Entry输入框判断输入内容
def reg():
    myAccount = a_entry.get()  # 获取⽤户输⼊的⽤户名
    myPassword = p_entry.get()  # 获取⽤户输⼊的密码
    a_len = len(myAccount)  # 获取输⼊的⽤户名⻓度
    p_len = len(myPassword)  # 获取输⼊的密码⻓度
    if myAccount == "itcast" and myPassword == "python":
        msg_label["text"] = "登录成功"  # ⽤户名和密码全部正确
    elif myAccount == "itcast" and myPassword != "python":
        msg_label["text"] = "密码错误"  # ⽤户名正确密码错误
        p_entry.delete(0, p_len)
    else:
        msg_label["text"] = "⽤户名错误"  # ⽤户名错误
        a_entry.delete(0, a_len)
        p_entry.delete(0, p_len)


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
    # ⽤户名
    a_label = Label(main_window, text="⽤户名：")
    a_label.grid(row=0, column=0, sticky=W)
    a_entry = Entry(main_window)
    a_entry.grid(row=0, column=1, sticky=E)
    # 密码
    p_label = Label(main_window, text="密码：")
    p_label.grid(row=1, column=0, sticky=W)
    p_entry = Entry(main_window)
    p_entry["show"] = "*"  # 密码显示为 *
    p_entry.grid(row=1, column=1, sticky=E)
    # 登录按钮
    btn = Button(main_window, text="登录", command=reg)
    btn.grid(row=2, column=1, sticky=E)
    # 提示信息
    msg_label = Label(main_window, text="")
    msg_label.grid(row=3)
    main_window.mainloop()
