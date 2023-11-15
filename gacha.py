import tkinter as tk
from tkinter import messagebox
import random
roll_time_char = 0
bảo_hiểm_char = 0
roll_time_vũ_khí = 0
bảo_hiểm_vũ_khí = 0
def roll_char():
    
    #xóa dữ liệu cũ
    Label1.destroy()
    button1.destroy()
    button2.destroy()
    
    #Bắt Đầu Roll
    def rolling():
        #đặt thông số
        global roll_time_char
        roll_time_char = roll_time_char + 10
        luck1 = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        num = random.randint(0,100)
        
        def nổ_vàng_char():
            global bảo_hiểm_char
            print(bảo_hiểm_char)
            global roll_time_char
            
            
            if bảo_hiểm_char == 1: #win
                messagebox.showinfo("Thắng GACHA RÒI", "KHÔNG LỆCH")
                bảo_hiểm_char = 0
                roll_time_char = 0
            elif num < 50:
                messagebox.showinfo("Thắng GACHA RÒI", "KHÔNG LỆCH")
                bảo_hiểm_char = 0
                roll_time_char = 0
            else:
                messagebox.showerror("LỆCH", "CHÚC MỪNG, M ĐÃ LỆCH RATE")
                bảo_hiểm_char = bảo_hiểm_char + 1
                roll_time_char = 0
        
        
        if num in luck1:
            nổ_vàng_char()
        elif roll_time_char >= 80:
            nổ_vàng_char()
        else:
            messagebox.showinfo("NỔ TÍM","CHƯA NỔ VÀNG")
    #tạo lable và button mới
    Label2 = tk.Label(window, text="Roll Nhân Vật")
    Label2.pack()
    button3 = tk.Button(window, text="ROLL", command= rolling)
    button3.pack()
def roll_vũ_khí():
    #xóa dữ liệu cũ
    Label1.destroy()
    button1.destroy()
    button2.destroy()
    
    
    label4 = tk.Label(window, text="ROLL VŨ KHÍ")
    label4.pack()
    #Bắt Đầu Roll
    def rolling_VK():
        #đặt thông số
        global roll_time_vũ_khí
        roll_time_vũ_khí = roll_time_vũ_khí + 10
        luck1 = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        num = random.randint(0,100)
        
        def nổ_vàng_vũ_khí():
            global bảo_hiểm_vũ_khí
            print(bảo_hiểm_vũ_khí)
            global roll_time_vũ_khí
            
            
            if bảo_hiểm_vũ_khí == 2: #win
                messagebox.showinfo("Thắng GACHA RÒI", "KHÔNG LỆCH")
                bảo_hiểm_vũ_khí = 0
                roll_time_vũ_khí = 0
            elif num < 50:
                messagebox.showinfo("Thắng GACHA RÒI", "KHÔNG LỆCH")
                bảo_hiểm_vũ_khí = 0
                roll_time_vũ_khí = 0
            else:
                messagebox.showerror("LỆCH", "CHÚC MỪNG, M ĐÃ LỆCH RATE")
                bảo_hiểm_vũ_khí = bảo_hiểm_vũ_khí + 1
                roll_time_vũ_khí = 0
                
                
        if num in luck1:
            nổ_vàng_vũ_khí()
        elif roll_time_vũ_khí >= 80:
            nổ_vàng_vũ_khí()
        else:
            messagebox.showinfo("NỔ TÍM","CHƯA NỔ VÀNG")
    Button3 = tk.Button(window, text="ROLL", command=rolling_VK)
    Button3.pack()
            
            
            
#Tạo của sổ
window = tk.Tk()
window.title("GENSHIN GACHA FUNNY")

#Tạo lable và button
Label1 = tk.Label(window, text="GACHA VŨ KHÍ HAY NHÂN VẬT")
Label1.pack()

button1 = tk.Button(window, text="Nhân Vật", width=7, height=1, command=roll_char)
button1.pack()
button2 = tk.Button(window, text="Vũ Khí", width=7, height=1, command=roll_vũ_khí)
button2.pack()


window.mainloop()