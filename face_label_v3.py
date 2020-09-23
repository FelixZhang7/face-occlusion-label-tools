from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from PIL import Image,ImageTk
import os
import glob

# 初始化
window = Tk()
# 设置窗口大小
window.geometry('800x520+500+100')

window.resizable(0, 0)  # 防止用户调整尺寸

# 设置标题
window.title('人脸遮挡标注小程序')

image_path = []
img_num = 0
num = 0


def select_file():
    global num
    global img_num
    global image_path
    chose_dir = tkinter.filedialog.askdirectory()
    path = glob.glob(os.path.join(chose_dir, '*.[jp][pn]g'))
    num = 0
    img_num = len(path)
    image_path = path
    if img_num == 0:
        tkinter.messagebox.showinfo(title='提示', message='当前文件夹文件没有图片!')
    else:
        var_path.set(image_path[0].replace('\\', '/'))
        img_open = Image.open(path[0]).resize((258, 258))
        image = ImageTk.PhotoImage(img_open)
        label_img.configure(image=image)
        label_img.image = image
        submit['state'] = NORMAL
        next_btn['state'] = NORMAL
        pre_btn['state'] = NORMAL


menubar = Menu(window)

filemenu = Menu(window, tearoff=0)
aboutmenu = Menu(window, tearoff=0)

menubar.add_cascade(label='文件', menu=filemenu)
menubar.add_cascade(label='关于', menu=aboutmenu)

filemenu.add_command(label='打开', command=select_file)
aboutmenu.add_command(label='版本号: 3.0')
aboutmenu.add_command(label='作者: 胡明越')

welcome = Label(window, text='欢迎进入人脸遮挡标注程序', fg='white', bg='#126bae', font=('Arial', 12), width=34, height=2).place(
    x=230, y=10)

tips = Label(window, text='(规则:此程序标注人脸7个部位有无遮挡，有遮挡标1，无遮挡标0)',
             fg='red', font=('Arial', 12), width=50, height=1).place(x=140, y=60)

# 第4步，在图形界面上设定输入框控件entry并放置控件
leye_label = Label(window, text='左侧眼睛:', font=('Arial', 14))
leye_var = IntVar()
leye_0 = Radiobutton(window, text='未遮挡', variable=leye_var, value=0, font=('Arial', 14), relief=GROOVE)
leye_1 = Radiobutton(window, text='遮挡', variable=leye_var, value=1, font=('Arial', 14), relief=GROOVE)
# left_eye = Entry(window, show=None, font=('Arial', 14),width=10)


reye_label = Label(window, text='右侧眼睛:', font=('Arial', 14))
reye_var = IntVar()
reye_0 = Radiobutton(window, text='未遮挡', variable=reye_var, value=0, font=('Arial', 14), relief=GROOVE)
reye_1 = Radiobutton(window, text='遮挡', variable=reye_var, value=1, font=('Arial', 14), relief=GROOVE)
# right_eye = Entry(window, show=None, font=('Arial', 14),width=10)

lcheck_label = Label(window, text='左脸颊:', font=('Arial', 14))
lcheck_var = IntVar()
lcheck_0 = Radiobutton(window, text='未遮挡', variable=lcheck_var, value=0, font=('Arial', 14), relief=GROOVE)
lcheck_1 = Radiobutton(window, text='遮挡', variable=lcheck_var, value=1, font=('Arial', 14), relief=GROOVE)
# left_check = Entry(window, show=None, font=('Arial', 14),width=10)

rcheck_label = Label(window, text='右脸颊:', font=('Arial', 14))
rcheck_var = IntVar()
rcheck_0 = Radiobutton(window, text='未遮挡', variable=rcheck_var, value=0, font=('Arial', 14), relief=GROOVE)
rcheck_1 = Radiobutton(window, text='遮挡', variable=rcheck_var, value=1, font=('Arial', 14), relief=GROOVE)
# right_check = Entry(window, show=None, font=('Arial', 14),width=10)

nose_label = Label(window, text='鼻子:', font=('Arial', 14))
nose_var = IntVar()
nose_0 = Radiobutton(window, text='未遮挡', variable=nose_var, value=0, font=('Arial', 14), relief=GROOVE)
nose_1 = Radiobutton(window, text='遮挡', variable=nose_var, value=1, font=('Arial', 14), relief=GROOVE)
# nose = Entry(window, show=None, font=('Arial', 14),width=10)

mouth_label = Label(window, text='嘴巴:', font=('Arial', 14))
mouth_var = IntVar()
mouth_0 = Radiobutton(window, text='未遮挡', variable=mouth_var, value=0, font=('Arial', 14), relief=GROOVE)
mouth_1 = Radiobutton(window, text='遮挡', variable=mouth_var, value=1, font=('Arial', 14), relief=GROOVE)
# mouth = Entry(window, show=None, font=('Arial', 14),width=10)

chin_label = Label(window, text='下巴:', font=('Arial', 14))
chin_var = IntVar()
chin_0 = Radiobutton(window, text='未遮挡', variable=chin_var, value=0, font=('Arial', 14), relief=GROOVE)
chin_1 = Radiobutton(window, text='遮挡', variable=chin_var, value=1, font=('Arial', 14), relief=GROOVE)
# chin = Entry(window, show=None, font=('Arial', 14),width=10)


img_open = Image.open('./welcome.jpg').resize((258, 258))
image = ImageTk.PhotoImage(img_open)
label_img = Label(window, image=image)
# label_img = Label(window)
label_img.place(x=100, y=100)


def next_img():
    global num
    global img_num
    global image_path
    num += 1
    #     num = num%img_num
    #     print(num,img_num)
    if num >= img_num:
        num = img_num - 1
        tkinter.messagebox.showinfo(title='提示', message='当前文件夹文件已标注完毕')
    # submit['state'] = DISABLED
    img_open = Image.open(image_path[num]).resize((258, 258))
    var_path.set(image_path[num].replace('\\', '/'))
    image = ImageTk.PhotoImage(img_open)
    label_img.configure(image=image)
    label_img.image = image


def pre_img():
    global num
    global img_num
    global image_path
    num -= 1
    #     print(num,img_num)
    if num < 0:
        num = 0
        tkinter.messagebox.showinfo(title='提示', message='啊偶！没有图片了')
    # submit['state'] = DISABLED
    img_open = Image.open(image_path[num]).resize((258, 258))
    var_path.set(image_path[num].replace('\\', '/'))
    image = ImageTk.PhotoImage(img_open)
    label_img.configure(image=image)
    label_img.image = image


def submit():
    # 标注逻辑
    if var_path.get() == '':
        tkinter.messagebox.showinfo(title='提示', message='path为空!')
    else:
        save_dir = os.path.split(var_path.get())[0]  # 文件夹
        txt_name = save_dir.split('/')[-1] + '_label.txt'
        with open(save_dir + '/' + txt_name, 'a') as f:
            path = var_path.get()
            leye_v = str(leye_var.get())
            reye_v = str(reye_var.get())
            lcheck_v = str(lcheck_var.get())
            rcheck_v = str(rcheck_var.get())
            nose_v = str(nose_var.get())
            mouth_v = str(mouth_var.get())
            chin_v = str(chin_var.get())
            label = leye_v + ' ' + reye_v + ' ' + lcheck_v + ' ' + rcheck_v + ' ' + nose_v + ' ' + mouth_v + ' ' + chin_v
            content = path + ',' + label + '\n'
            print(content.strip())
            f.write(content)


next_btn = Button(window, text='下一张', font=('Arial', 12), fg='white', width=10, height=1, command=next_img,
                  bg='#126bae', state=DISABLED)
pre_btn = Button(window, text='上一张', font=('Arial', 12), fg='white', width=10, height=1, command=pre_img, bg='#126bae',
                 state=DISABLED)

submit = Button(window, text='提交', font=('Arial', 12), fg='white', width=10, height=1, command=submit, bg='#126bae',
                state=DISABLED)
var_path = StringVar()
path = Label(window, textvariable=var_path,
             highlightcolor='red', font=('Arial', 12), width=70, height=1).place(x=70, y=420)

###布局
leye_label.place(x=450, y=100)
# left_eye.place(x=550,y=100)
leye_0.place(x=550, y=100)
leye_1.place(x=650, y=100)

reye_label.place(x=450, y=140)
# right_eye.place(x=550,y=140)
reye_0.place(x=550, y=140)
reye_1.place(x=650, y=140)

lcheck_label.place(x=450, y=180)
# left_check.place(x=550,y=180)
lcheck_0.place(x=550, y=180)
lcheck_1.place(x=650, y=180)

rcheck_label.place(x=450, y=220)
# right_check.place(x=550,y=220)
rcheck_0.place(x=550, y=220)
rcheck_1.place(x=650, y=220)

nose_label.place(x=450, y=260)
# nose.place(x=550,y=260)
nose_0.place(x=550, y=260)
nose_1.place(x=650, y=260)

mouth_label.place(x=450, y=300)
# mouth.place(x=550,y=300)
mouth_0.place(x=550, y=300)
mouth_1.place(x=650, y=300)

chin_label.place(x=450, y=340)
# chin.place(x=550,y=340)
chin_0.place(x=550, y=340)
chin_1.place(x=650, y=340)
pre_btn.place(x=450, y=380)
next_btn.place(x=555, y=380)
submit.place(x=660, y=380)
window.config(menu=menubar)
window.mainloop()


