"""
Author:humingyue
Time:20201201
File:face_label.py
Software:Pycharm
"""
from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image, ImageTk
import os
import glob


class FaceLabel:
    def __init__(self, init_window_name):
        self.window = init_window_name
        self.image_path = []
        self.img_num = 0
        self.num = 0
        self.welcome_path = './welcome.jpg'  # 首页图片

    def set_init_window(self):
        self.window.geometry('800x520+500+100')
        self.window.resizable(0, 0)  # 防止用户调整尺寸
        # 设置标题
        self.window.title('人脸遮挡标注小程序')
        self.menubar = Menu(window)
        self.filemenu = Menu(window, tearoff=0)
        self.aboutmenu = Menu(window, tearoff=0)
        self.menubar.add_cascade(label='文件', menu=self.filemenu)
        self.menubar.add_cascade(label='关于', menu=self.aboutmenu)

        self.filemenu.add_command(label='打开', command=self.select_file)
        self.aboutmenu.add_command(label='版本号: 3.0')
        self.aboutmenu.add_command(label='作者: 胡明越')
        self.welcome = Label(self.window, text='欢迎进入人脸遮挡标注程序', fg='white', bg='#126bae', font=('Arial', 12), width=34,
                             height=2).place(
            x=230, y=10)
        self.tips = Label(self.window, text='(规则:此程序标注人脸7个部位有无遮挡，有遮挡标1，无遮挡标0)',
                          fg='red', font=('Arial', 12), width=50, height=1).place(x=140, y=60)

        # 第4步，在图形界面上设定输入框控件entry并放置控件
        self.leye_label = Label(self.window, text='左侧眼睛:', font=('Arial', 14))
        self.leye_var = IntVar()
        self.leye_0 = Radiobutton(self.window, text='未遮挡', variable=self.leye_var, value=0, font=('Arial', 14),
                                  relief=GROOVE)
        self.leye_1 = Radiobutton(self.window, text='遮挡', variable=self.leye_var, value=1, font=('Arial', 14),
                                  relief=GROOVE)

        self.reye_label = Label(self.window, text='右侧眼睛:', font=('Arial', 14))
        self.reye_var = IntVar()
        self.reye_0 = Radiobutton(self.window, text='未遮挡', variable=self.reye_var, value=0, font=('Arial', 14),
                                  relief=GROOVE)
        self.reye_1 = Radiobutton(self.window, text='遮挡', variable=self.reye_var, value=1, font=('Arial', 14),
                                  relief=GROOVE)

        self.lcheck_label = Label(self.window, text='左脸颊:', font=('Arial', 14))
        self.lcheck_var = IntVar()
        self.lcheck_0 = Radiobutton(self.window, text='未遮挡', variable=self.lcheck_var, value=0, font=('Arial', 14),
                                    relief=GROOVE)
        self.lcheck_1 = Radiobutton(self.window, text='遮挡', variable=self.lcheck_var, value=1, font=('Arial', 14),
                                    relief=GROOVE)

        self.rcheck_label = Label(self.window, text='右脸颊:', font=('Arial', 14))
        self.rcheck_var = IntVar()
        self.rcheck_0 = Radiobutton(self.window, text='未遮挡', variable=self.rcheck_var, value=0, font=('Arial', 14),
                                    relief=GROOVE)
        self.rcheck_1 = Radiobutton(self.window, text='遮挡', variable=self.rcheck_var, value=1, font=('Arial', 14),
                                    relief=GROOVE)

        self.nose_label = Label(self.window, text='鼻子:', font=('Arial', 14))
        self.nose_var = IntVar()
        self.nose_0 = Radiobutton(self.window, text='未遮挡', variable=self.nose_var, value=0, font=('Arial', 14),
                                  relief=GROOVE)
        self.nose_1 = Radiobutton(self.window, text='遮挡', variable=self.nose_var, value=1, font=('Arial', 14),
                                  relief=GROOVE)

        self.mouth_label = Label(self.window, text='嘴巴:', font=('Arial', 14))
        self.mouth_var = IntVar()
        self.mouth_0 = Radiobutton(self.window, text='未遮挡', variable=self.mouth_var, value=0, font=('Arial', 14),
                                   relief=GROOVE)
        self.mouth_1 = Radiobutton(self.window, text='遮挡', variable=self.mouth_var, value=1, font=('Arial', 14),
                                   relief=GROOVE)

        self.chin_label = Label(self.window, text='下巴:', font=('Arial', 14))
        self.chin_var = IntVar()
        self.chin_0 = Radiobutton(self.window, text='未遮挡', variable=self.chin_var, value=0, font=('Arial', 14),
                                  relief=GROOVE)
        self.chin_1 = Radiobutton(self.window, text='遮挡', variable=self.chin_var, value=1, font=('Arial', 14),
                                  relief=GROOVE)
        self.img_open = Image.open(self.welcome_path).resize((258, 258))
        self.image = ImageTk.PhotoImage(self.img_open)
        self.label_img = Label(self.window, image=self.image)
        self.label_img.place(x=100, y=100)

        self.next_btn = Button(self.window, text='下一张', font=('Arial', 12), fg='white', width=10, height=1,
                               command=self.next_img,
                               bg='#126bae', state=DISABLED)
        self.pre_btn = Button(self.window, text='上一张', font=('Arial', 12), fg='white', width=10, height=1,
                              command=self.pre_img,
                              bg='#126bae',
                              state=DISABLED)

        self.submit = Button(self.window, text='提交', font=('Arial', 12), fg='white', width=10, height=1,
                             command=self.submit,
                             bg='#126bae',
                             state=DISABLED)
        self.var_path = StringVar()
        self.path = Label(self.window, textvariable=self.var_path,
                          highlightcolor='red', font=('Arial', 12), width=70, height=1).place(x=70, y=420)

        ###布局
        self.leye_label.place(x=450, y=100)
        self.leye_0.place(x=550, y=100)
        self.leye_1.place(x=650, y=100)

        self.reye_label.place(x=450, y=140)
        self.reye_0.place(x=550, y=140)
        self.reye_1.place(x=650, y=140)

        self.lcheck_label.place(x=450, y=180)
        self.lcheck_0.place(x=550, y=180)
        self.lcheck_1.place(x=650, y=180)

        self.rcheck_label.place(x=450, y=220)
        self.rcheck_0.place(x=550, y=220)
        self.rcheck_1.place(x=650, y=220)

        self.nose_label.place(x=450, y=260)
        self.nose_0.place(x=550, y=260)
        self.nose_1.place(x=650, y=260)

        self.mouth_label.place(x=450, y=300)
        self.mouth_0.place(x=550, y=300)
        self.mouth_1.place(x=650, y=300)

        self.chin_label.place(x=450, y=340)
        self.chin_0.place(x=550, y=340)
        self.chin_1.place(x=650, y=340)
        self.pre_btn.place(x=450, y=380)
        self.next_btn.place(x=555, y=380)
        self.submit.place(x=660, y=380)

        self.window.config(menu=self.menubar)
        self.window.mainloop()

    def select_file(self):
        chose_dir = tkinter.filedialog.askdirectory()
        path = glob.glob(os.path.join(chose_dir, '*.[jp][pn]g'))
        self.num = 0
        self.img_num = len(path)
        self.image_path = path
        if self.img_num == 0:
            tkinter.messagebox.showinfo(title='提示', message='当前文件夹文件没有图片!')
        else:
            self.var_path.set(self.image_path[0].replace('\\', '/'))
            img_open = Image.open(path[0]).resize((258, 258))
            image = ImageTk.PhotoImage(img_open)
            self.label_img.configure(image=image)
            self.label_img.image = image
            self.submit['state'] = NORMAL
            self.next_btn['state'] = NORMAL
            self.pre_btn['state'] = NORMAL

    def next_img(self):
        self.num += 1
        if self.num >= self.img_num:
            self.num = self.img_num - 1
            tkinter.messagebox.showinfo(title='提示', message='当前文件夹文件已标注完毕')
        # submit['state'] = DISABLED
        img_open = Image.open(self.image_path[self.num]).resize((258, 258))
        self.var_path.set(self.image_path[self.num].replace('\\', '/'))
        image = ImageTk.PhotoImage(img_open)
        self.label_img.configure(image=image)
        self.label_img.image = image

    def pre_img(self):
        self.num -= 1
        #     print(num,img_num)
        if self.num < 0:
            self.num = 0
            tkinter.messagebox.showinfo(title='提示', message='啊偶！没有图片了')
        # submit['state'] = DISABLED
        img_open = Image.open(self.image_path[self.num]).resize((258, 258))
        self.var_path.set(self.image_path[self.num].replace('\\', '/'))
        image = ImageTk.PhotoImage(img_open)
        self.label_img.configure(image=image)
        self.label_img.image = image

    def submit(self):
        # 标注逻辑
        if self.var_path.get() == '':
            tkinter.messagebox.showinfo(title='提示', message='path为空!')
        else:
            save_dir = os.path.split(self.var_path.get())[0]  # 文件夹
            txt_name = save_dir.split('/')[-1] + '_label.txt'
            with open(save_dir + '/' + txt_name, 'a') as f:
                path = self.var_path.get()
                leye_v = str(self.leye_var.get())
                reye_v = str(self.reye_var.get())
                lcheck_v = str(self.lcheck_var.get())
                rcheck_v = str(self.rcheck_var.get())
                nose_v = str(self.nose_var.get())
                mouth_v = str(self.mouth_var.get())
                chin_v = str(self.chin_var.get())
                label = leye_v + ' ' + reye_v + ' ' + lcheck_v + ' ' + rcheck_v + ' ' + nose_v + ' ' + mouth_v + ' ' + chin_v
                content = path + ',' + label + '\n'
                print(content.strip())
                f.write(content)


# 初始化
window = Tk()
face_label = FaceLabel(window)
face_label.set_init_window()
