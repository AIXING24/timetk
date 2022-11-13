import time
from tkinter import *
from pygame import mixer

def run1():
    a = int(inp1.get())
    s = a*60
    while s > 0:
        txt.insert(END, s-1)
        time.sleep(1)
        txt.update()
        txt.delete(0.0, END)  # 清空输出
        s = s-1
    if s == 0:
        mixer.init()
        mixer.music.load('12225.mp3')
        mixer.music.play(loops=100, start=0)
        time.sleep(20)
        mixer.music.stop()
        while True:
            pass


root = Tk()
root.geometry('460x240')
root.title('TIME')

lb1 = Label(root, text='input（min）')
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)
btn1 = Button(root, text='click', command=run1)
btn1.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.1)

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(root)
txt.place(rely=0.6, relheight=0.4)
root.mainloop()

