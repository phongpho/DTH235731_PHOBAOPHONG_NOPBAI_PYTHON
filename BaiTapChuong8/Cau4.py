from tkinter import *

# ====== HÀM XỬ LÝ ======
def insertGiaTri(giaTri):
    hienThi.insert(END, giaTri)

def delete():
    hienThi.delete(0, END)

def tinhToan():
    try:
        kq = eval(hienThi.get())
        hienThi.delete(0, END)
        hienThi.insert(END, str(kq))
    except:
        hienThi.delete(0, END)
        hienThi.insert(END, "Lỗi!")

# ====== GIAO DIỆN ======
root = Tk()


# Ô hiển thị
hienThi = Entry(root, width=17, font=("tahoma", 16), justify="right")
hienThi.pack(pady=8)

# ====== KHUNG CHÍNH ======
frameChinh = Frame(root)
frameChinh.pack()

# ====== HÀNG 1 ======
frame1 = Frame(frameChinh)
frame1.pack()
Button(frame1, text="1", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("1")).pack(side=LEFT, padx=1, pady=1)
Button(frame1, text="2", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("2")).pack(side=LEFT, padx=1, pady=1)
Button(frame1, text="3", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("3")).pack(side=LEFT, padx=1, pady=1)

# ====== HÀNG 2 ======
frame2 = Frame(frameChinh)
frame2.pack()
Button(frame2, text="4", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("4")).pack(side=LEFT, padx=1, pady=1)
Button(frame2, text="5", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("5")).pack(side=LEFT, padx=1, pady=1)
Button(frame2, text="6", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("6")).pack(side=LEFT, padx=1, pady=1)

# ====== HÀNG 3 ======
frame3 = Frame(frameChinh)
frame3.pack()
Button(frame3, text="7", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("7")).pack(side=LEFT, padx=1, pady=1)
Button(frame3, text="8", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("8")).pack(side=LEFT, padx=1, pady=1)
Button(frame3, text="9", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("9")).pack(side=LEFT, padx=1, pady=1)

# ====== HÀNG 4 ======
frame4 = Frame(frameChinh)
frame4.pack()
Button(frame4, text="-", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("-")).pack(side=LEFT, padx=1, pady=1)
Button(frame4, text="0", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("0")).pack(side=LEFT, padx=1, pady=1)
Button(frame4, text=".", width=6, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri(".")).pack(side=LEFT, padx=1, pady=1)

# ====== HÀNG 5 (width = 3) ======
frame5 = Frame(frameChinh)
frame5.pack()
Button(frame5, text="+", width=3, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("+")).pack(side=LEFT, padx=1, pady=1)
Button(frame5, text="-", width=3, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("-")).pack(side=LEFT, padx=1, pady=1)
Button(frame5, text="*", width=3, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("*")).pack(side=LEFT, padx=1, pady=1)
Button(frame5, text="/", width=3, height=2, font=("tahoma", 12),
       command=lambda: insertGiaTri("/")).pack(side=LEFT, padx=1, pady=1)
Button(frame5, text="=", width=3, height=2, font=("tahoma", 12),
       command=tinhToan).pack(side=LEFT, padx=1, pady=1)

# ====== HÀNG 6 (nút Xóa) ======
frame6 = Frame(frameChinh)
frame6.pack()
Button(frame6, text="Clr", width=21, height=2, font=("tahoma", 12),
       command=delete).pack(side=LEFT, padx=1, pady=1)

root.mainloop()
