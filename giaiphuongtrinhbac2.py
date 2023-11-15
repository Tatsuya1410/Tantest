# Giải Phương Trình BẬc 2 dùng Python - @Tânn Mguyễn

# Import
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

math1 = Tk()
math1.geometry('350x250')

# xử lý button
def exit():
    quit()
def submit():
    Ai = A.get()
    Bi = B.get()
    Ci = C.get()
    if int(Ai) == 0:
        messagebox.showerror('A > 0')
        quit()
    # tính Delta
    Delta = (int(Bi)**2)-4*(int(Ai))*(int(Ci))
    if Delta < 0:
        messagebox.showerror("S = ∅")
        
    elif Delta == 0:
        x1 = x2 = -(int(Bi))/(2*int(Ai))
    
    else:
        x1 = (-int(Bi)+(int(Delta)**.5))/(2*int(Ai))
        x2 = (-int(Bi)-(int(Delta)**.5))/(2*int(Ai))
        x3 = round(x1,5)
        x4 = round(x2,5)

# trả nghiệm
    Label(math1, text= "delta là: " + str(Delta)).place(x= 130, y= 140)
    Label(math1, text= "Nghiệm của x1 là: " + str(x3)).place(x= 130, y= 170)
    Label(math1, text= "Nghiệm của x2 là: " + str(x4)).place(x= 130, y= 200)

tx_img = ImageTk.PhotoImage(Image.open("E:/python/code space/giải pt bậc 2/Color_circle_(RGB).png"))
tximg =Label(math1, image= tx_img)
tximg.place(x= 0, y=0, relwidth=1, relheight=1)
A = Label(math1, text="Nhập số A, B, C", fg= 'red' ).place(x= 130, y= 85)
    
# tạo bảng nhập số liệu

A = Entry(math1)
A.pack()
B = Entry(math1)
B.pack()
C = Entry(math1)
C.pack()

print()

submit = Button(math1, text="Nhập", bg= 'black', fg= 'white', command=submit).place(x= 155, y= 105)
exit = Button(math1, text="xóa", bg= 'red', fg= 'white', command=exit).place(x= 320, y= 225)

math1.mainloop()