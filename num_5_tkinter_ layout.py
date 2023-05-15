"""
    tkinter_布局管理:
        三种布局:
            1. pack布局:
                调用pack()函数来将组件放置在窗口对象中如果不传参, 会给组件⼀个⾃认为合适的位置和⼤⼩, 这是默认的布局方式
                pack()函数参数:
                    side: 指定组件停靠⽅向, 可以为 LEFT, TOP, RIGHT, BOTTOM, 分别代表 左, 上, 右, 下
                    fill: 指定组件填充方向, 可以是 X, Y, BOTH 和 NONE, 即在⽔平⽅向填充, 竖直⽅向填充, ⽔平和竖直⽅向填充和不填充
                    expand: 指定组件的大小是否从"势力范围"扩大到"扩展范围", 可以是YES或NO
                    anchor: 决定组件停靠的位置, 可以是 N, E, S, W以及他们的组合或者是 CENTER(表示中间)
                        N ==> 北 ==> 上, E ==> 东 ==> 右, S ==> 南 ==> 下, W ==> 西 ==> 左
                    padx / pady: 组件外, 组件跟邻近组件或窗体边界的距离(外边距), 默认值为0
                    ipadx/ipady: 组件内, 组件文本跟组件边界之间的距离(内边距), 默认值为0
            2. grid布局:
                也叫网格布局, 调用grid()函数来将组件放置在窗口对象
                grid()函数参数:
                    row / column: 表示行或列, 编号从 0 开始
                    rowspan / columnspan: 表示跨越的行数或列数
                    padx / pady: 组件外, 组件跟邻近组件或窗体边界的距离(外边距), 默认值为0
                    ipadx/ipady: 组件内, 组件文本跟组件边界之间的距离(内边距), 默认值为0
                    sticky: 当表格框大小组件的大小, 组件默认居中显示, 那这个表格框周围的空白部分, 如何分配, 这就由sticky来决定
                        具体规定如下:
                            默认组件在表格框中是居中对齐显示的, 但通过sticky可以设定N/S/W/E 即上/下/左/右 对齐,
                            N/S/W/E 也可以组合使用, 如：
                                sticky=N+S 拉高组件, 让组件上下填充到表格框的顶端和底端
                                sticky=N+S+E 拉高组件, 让组件上下填充到表格框的顶端和底端, 同时, 让组件靠右对齐。
                                sticky=N+W+W+E 拉高并拉长组件, 让组件填充满一个表格框。
                                其它的, 以此类推……
            3. place布局:
                分为绝对布局与相对布局
                绝对布局:
                    参数为 x / y, 单位为像素, 默认主窗口左上角为 x = 0, y = 0
                相对布局:
                    width: 指组件的宽度, 单位是像素
                    height: 指组件的高度, 单位是像素
                    relwidth: 指组件相对于父组件的宽度, 取值范围为0-1; 跟父组件一样宽, 就取1, 只有一半宽, 就取0.5, 以此类推
                    relheight: 指组件相对于父组件的高度, 取值范围为0-1; 跟父组件一样高, 就取1, 只有一半宽, 就取0.5, 以此类推
                relwidth/relheight 和 x / y 可以组合在一起使用:
                    系统会优先取relwidth/relheight的值, 定位组件的位置后, 再以这个位置为起始点, 再根据x/y的值 再调整到新位置, x/y可以取负值
                place布局方法不常使用, 了解即可
"""
from tkinter import *


def pack_layout_test():
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
    Button(main_window, text="A").pack(side=LEFT, expand=YES, fill=Y)
    Button(main_window, text="B").pack(side=TOP, expand=YES, fill=BOTH)
    Button(main_window, text="C").pack(side=RIGHT, expand=YES, fill=NONE, anchor=NE)
    Button(main_window, text="D").pack(side=LEFT, expand=NO, fill=Y)
    Button(main_window, text="E").pack(side=TOP, expand=NO, fill=Y)
    Button(main_window, text="F").pack(side=BOTTOM, expand=YES)
    Button(main_window, text="G").pack(anchor=SE)
    main_window.mainloop()


def grid_layout_test():
    root = Tk()

    la1 = Label(root, text='用户名：')
    la1.grid(row=0, column=0)  # 0行0列

    en1 = Entry(root)  # 用户名文本框
    en1.grid(row=0, column=1, columnspan=2)  # 0行1列, 跨2列

    la2 = Label(root, text='密　码：')
    la2.grid(row=1, column=0)

    en2 = Entry(root)  # 密码文本框
    en2.grid(row=1, column=1, columnspan=2)  # 1行1列, 跨2列

    but1 = Button(root, text="确定")
    but1.grid(row=2, column=1)
    but2 = Button(root, text="取消")
    but2.grid(row=2, column=2)

    root.mainloop()


if __name__ == '__main__':
    pack_layout_test()
    grid_layout_test()
    pass
