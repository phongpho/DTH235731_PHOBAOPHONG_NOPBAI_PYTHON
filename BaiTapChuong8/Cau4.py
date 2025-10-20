from tkinter import *

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


root = Tk()
root.minsize(height=150, width=200)


hienThi = Entry(root, font=("tahoma", 16), justify="right")
hienThi.grid(row=0, columnspan=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#1
frame1 = Frame(root)
frame1.grid(row=1, column=0, columnspan=3, sticky="we")
Button(frame1, text="1", font=("tahoma", 12), command=lambda: insertGiaTri("1")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame1, text="2", font=("tahoma", 12), command=lambda: insertGiaTri("2")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame1, text="3", font=("tahoma", 12), command=lambda: insertGiaTri("3")).pack(side=LEFT, expand=True, fill=BOTH)

#2
frame2 = Frame(root)
frame2.grid(row=2, column=0, columnspan=3, sticky="we")
Button(frame2, text="4", font=("tahoma", 12), command=lambda: insertGiaTri("4")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame2, text="5", font=("tahoma", 12), command=lambda: insertGiaTri("5")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame2, text="6", font=("tahoma", 12), command=lambda: insertGiaTri("6")).pack(side=LEFT, expand=True, fill=BOTH)

#3
frame3 = Frame(root)
frame3.grid(row=3, column=0, columnspan=3, sticky="we")
Button(frame3, text="7", font=("tahoma", 12), command=lambda: insertGiaTri("7")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame3, text="8", font=("tahoma", 12), command=lambda: insertGiaTri("8")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame3, text="9", font=("tahoma", 12), command=lambda: insertGiaTri("9")).pack(side=LEFT, expand=True, fill=BOTH)

#4
frame4 = Frame(root)
frame4.grid(row=4, column=0, columnspan=3, sticky="we")
Button(frame4, text="-", font=("tahoma", 12), command=lambda: insertGiaTri("-")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame4, text="0", font=("tahoma", 12), command=lambda: insertGiaTri("0")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame4, text=".", font=("tahoma", 12), command=lambda: insertGiaTri(".")).pack(side=LEFT, expand=True, fill=BOTH)

#5
frame5 = Frame(root)
frame5.grid(row=5, column=0, columnspan=3, sticky="we")
Button(frame5, text="+", font=("tahoma", 12), command=lambda: insertGiaTri("+")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame5, text="-", font=("tahoma", 12), command=lambda: insertGiaTri("-")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame5, text="*", font=("tahoma", 12), command=lambda: insertGiaTri("*")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame5, text="/", font=("tahoma", 12), command=lambda: insertGiaTri("/")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame5, text="=", font=("tahoma", 12), command=tinhToan).pack(side=LEFT, expand=True, fill=BOTH)

#6
frame6 = Frame(root)
frame6.grid(row=6, column=0, columnspan=3, sticky="we")
Button(frame6, text="Clr", font=("tahoma", 12), command=delete).pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()