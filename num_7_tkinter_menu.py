"""
    tkinter_菜单:
        菜单的信息量是⾮常巨⼤的, 由于菜单⼜可以有⼦菜单, 因此菜单的信息量⾮常⼤
        菜单通常可以分为下拉菜单和弹出菜单
        创建菜单:
            menu_object = Menu(window_name)
        添加菜单项:
            menu_object.add_command(label = menu_name)
            add_command()方法:
                label ==> 指定菜单项的名称
                command ==> 指定被点击时调用的方法
                acceletor ==> 指定快捷键
                underline ==> 指定是否有下划线
        指定顶层菜单:
            使用窗口对象的'menu'属性来指定顶层菜单
            window_name['menu'] = menu_object_name
        添加子菜单:
            1. 先创建顶层菜单对象
                menu_top_object = Menu(window_name)
            2. 创建子菜单对象, 绑定顶层菜单对象
                menu_child_object = Menu(menu_top_object)
            3. 为子菜单添加菜单项
                menu_child_object.add_command(label = menu_name)
            4. 顶层菜单对象调用 add_cascade() 方法为顶层菜单添加菜单项并级联子菜单
                menu_top_object.add_cascade(label = menu_name, menu=menu_child_object)
                label ==> 指定菜单项的名称
                menu ==> 指定将哪个子菜单级联到该菜单项
            注意: 添加子菜单要先处理子菜单, 最后再处理顶层菜单
        弹出菜单:
            ⼜叫上下⽂菜单, 也叫右键菜单, 通常是鼠标单击右键产生的菜单, tkinter里面没有弹出菜单简单的制作方法,
            因此只能使用事件绑定的方式来实现
            实现思路:
                1. 新建菜单对象
                2. 添加菜单项
                3. 定义函数, 函数中调用 Menu 类的 post ⽅法弹出菜单
                    post()方法: 接收两个参数, 即 x 和 y 坐标, 该方法会在相应的位置弹出菜单
        插入分割线:
            子菜单中还可以插入分割线来表示分割线上下属于不同的类别
            使用子菜单对象在要插入分割线的位置调用 add_separator() 方法即可, 该方法无需传参
            即: menu_child_object.add_separator()
        单选菜单和复选菜单:
            添加单选菜单: menu_child_object.add_radiobutton()
            添加复选菜单: menu_child_object.add_checkbutton()
            使用时与 add_command() 方法类似, 当被标记为单选或复选菜单时, 选中对应菜单项会在菜单项前面出现一个对号标记
            单选菜单一次只能选中一个菜单项, 复选菜单一次可以选中多个菜单项

"""
from tkinter import *


# 定义函数, 创建顶层菜单
def creat_top_menu():
    global main_window
    # 创建菜单对象
    menu_top = Menu(main_window)
    # 为菜单对象添加菜单项
    menu_top.add_command(label="文件")
    menu_top.add_command(label="编辑")
    menu_top.add_command(label="视图")
    menu_top.add_command(label="关于")
    # 设置顶层菜单
    main_window['menu'] = menu_top
    # 调用 mainloop() 方法
    main_window.mainloop()
    pass


# 定义函数, 创建子菜单
def creat_child_menu():
    global main_window
    # 创建顶层菜单对象
    menu_top = Menu(main_window)
    # 创建'文件'级联子菜单对象
    file_menu = Menu(menu_top)
    # '文件'级联子菜单添加菜单项
    for item in ["新建", "打开", "保存", "另存为", "退出"]:
        file_menu.add_command(label=item)
    # 创建'编辑'级联子菜单对象
    edit_menu = Menu(menu_top)
    # '编辑'级联子菜单添加菜单项
    for item in ["复制", "粘贴", "剪切", "撤销"]:
        edit_menu.add_command(label=item)
    # 创建'视图'级联子菜单对象
    view_menu = Menu(menu_top)
    # '视图'级联子菜单添加菜单项
    for item in ["默认视图", "全屏模式", "显示/隐藏菜单"]:
        view_menu.add_command(label=item)
    # 创建'关于'级联子菜单对象
    about_menu = Menu(menu_top)
    # '关于'级联子菜单添加菜单项
    for item in ["版权信息", "帮助⽂档"]:
        about_menu.add_command(label=item)
    # 顶层菜单添加菜单项并绑定级联菜单
    menu_top.add_cascade(label='文件', menu=file_menu)
    menu_top.add_cascade(label='编辑', menu=edit_menu)
    menu_top.add_cascade(label='视图', menu=view_menu)
    menu_top.add_cascade(label='关于', menu=about_menu)
    # 指定窗口顶级菜单
    main_window['menu'] = menu_top


def my_python():
    global main_window
    Label(main_window, text="我的Python课程").pack()  # 点击Python后添加这个标签


# 定义函数, 创建弹出菜单
def creat_pop_up_menu():
    global main_window
    menu_bar = Menu(main_window)
    for each in ["C/C++", "JavaEE", "Android", "PHP", "UI设计", "iOS", "前端与移动开发", "⽹络营销", "云计算"]:
        menu_bar.add_command(label=each)
    menu_bar.add_command(label="Python", command=my_python)

    # 定义内函数, 用于事件绑定
    def pop_up(event):
        menu_bar.post(event.x_root, event.y_root)

    main_window.bind('<Button-3>', pop_up)
    pass


# 定义函数, 插入分割线
def insert_sep():
    global main_window
    # 创建顶层菜单对象
    menu_object = Menu(main_window)
    # 创建子菜单对象
    menu_child_object = Menu(menu_object)
    # 为子菜单对象添加第一部分菜单项
    for each in ["C/C++", "Python", "JavaEE", "Android", "iOS", "云计算"]:
        menu_child_object.add_command(label=each)
    # 插入分割线
    menu_child_object.add_separator()
    # 为子菜单对象添加第二部分菜单项
    for each in ["PHP", "UI设计", "前端与移动开发", "⽹络营销"]:
        menu_child_object.add_command(label=each)
    # 为顶层菜单添加菜单项并级联子菜单
    menu_object.add_cascade(label="学科列表", menu=menu_child_object)
    # 指定窗口对象顶层菜单
    main_window['menu'] = menu_object


# 定义函数, 添加单选菜单和复选菜单
def radio_check_menu():
    global main_window
    # 创建顶层菜单对象
    menu_object = Menu(main_window)
    # 创建子菜单对象
    menu_child_object = Menu(menu_object)
    # 为子菜单对象添加第一部分菜单项, 该部分定义为单选菜单
    for each in ["C/C++", "Python", "JavaEE", "Android", "iOS", "云计算"]:
        menu_child_object.add_radiobutton(label=each)
    # 插入分割线
    menu_child_object.add_separator()
    # 为子菜单对象添加第二部分菜单项, 该部分定义为复选菜单
    for each in ["PHP", "UI设计", "前端与移动开发", "⽹络营销"]:
        menu_child_object.add_checkbutton(label=each)
    # 为顶层菜单添加菜单项并级联子菜单
    menu_object.add_cascade(label="学科列表", menu=menu_child_object)
    # 指定窗口对象顶层菜单
    main_window['menu'] = menu_object


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
    radio_check_menu()
    # 调用mainloop()方法
    main_window.mainloop()
    pass
