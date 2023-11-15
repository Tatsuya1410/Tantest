from tkinter import *
from tkinter import messagebox
import random

# tạo sự kiện cho btn
def no():
    messagebox.showinfo(' ', 'juan luon anh')
    quit()

def motionMouse(event):
    btnYes.place(x= random.randint(0,500), y= random.randint(0,500))

# tạo cửa sổ root
root = Tk()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'black'

# tạo btn
Label = Label(root, text='mày gay à?', font= 'Arial 15 bold', bg= 'white').pack()
btnYes = Button(root, text = 'đéo', font= 'Arial 15 bold')
btnYes.place(x= 170, y= 100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text= 'Đ-đúng', font= 'Arial 15 bold', command=no).place(x=350, y=100)

root.mainloop()