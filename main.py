import ttkbootstrap.dialogs
from ttkbootstrap import *
from ttkbootstrap.constants import *


class report():
    def __init__(self):
        self.add_num = 1
        self.rp = Window()
        # 设置程序标题
        self.rp.title('report')
        # 设置主程序窗口大小
        self.rp.geometry('900x700')
        self.main()

    def del_line(self, frame):
        if self.add_num > 1:
            frame.destroy()
            self.add_num -= 1
        else:
            ttkbootstrap.dialogs.Messagebox.show_info(title="提示", message="最少保留一行！")

    def add_line(self):
        # 添加一个frame
        frame_text = Frame(self.frame2)
        frame_text.pack(side=TOP, pady=(20, 0))
        # 给frame放一个文本框
        entry1 = Entry(frame_text, bootstyle=SUCCESS, width=50, font=('', 14))
        entry1.pack(anchor='nw', side=LEFT, padx=(20, 0))
        # 给frame放一个按钮，跟文本框并排
        btn_del = Button(frame_text, bootstyle='danger', text='删除', command=lambda: self.del_line(frame_text))
        btn_del.pack(anchor='n', side=LEFT, padx=10)

    def btn_add_line(self):
        if self.add_num < 5:
            self.add_num += 1
            self.add_line()
        else:
            ttkbootstrap.dialogs.Messagebox.show_info(title="提示", message="最多添加5行！")


    def main(self):
        # 本周任务
        self.frame1 = Frame(self.rp)
        self.frame1.pack()
        label1 = Label(self.frame1, text="todo", bootstyle=SUCCESS, font=('', 30))
        label1.pack()
        # 添加一个frame
        self.frame2 = Frame(self.frame1)
        self.frame2.pack()
        self.add_line()

        btn_add = Button(self.frame1, bootstyle=SUCCESS, text='添加')
        btn_add.config(command=self.btn_add_line, width=15)
        btn_add.pack(anchor='w', side=LEFT, pady=(10, 0), padx=(100, 50))

        btn_sub = Button(self.frame1, bootstyle='primary', text='提交')
        btn_sub.config(command=self.btn_add_line, width=15)
        btn_sub.pack(anchor='e', side=LEFT, pady=(10, 0), padx=(100, 100))



        # 下周计划

        self.rp.mainloop()


if __name__ == '__main__':
    report()
