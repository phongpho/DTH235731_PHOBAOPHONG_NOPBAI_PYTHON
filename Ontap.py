from tkinter import *

def insertA(giatri):
    entry.insert(END, giatri)

def tinh():
    try:
        kq = eval(entry.get())
        entry.delete(0,END)
        entry.insert(END, str(kq))
    except:
        entry.delete(0,END)
        entry.insert(END, 'Lỗi!')

def delete():
    entry.delete(0, END)

root = Tk()
root.geometry('225x230')
root.resizable(height=True, width=True)

entry = Entry(root, font=('tahoma',16), justify="right")
entry.grid(row=0, columnspan=3)

#1
frame1 = Frame(root)
frame1.grid(row=1, column=0, columnspan=3, sticky="we")
Button(frame1, text="1", font=("tahoma", 12), command=lambda: insertA("1")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame1, text="2", font=("tahoma", 12), command=lambda: insertA("2")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame1, text="3", font=("tahoma", 12), command=lambda: insertA("3")).pack(side=LEFT, expand=True, fill=BOTH)

#2
frame2 = Frame(root)
frame2.grid(row=2, column=0, columnspan=3, sticky="we")
Button(frame2, text="4", font=("tahoma", 12), command=lambda: insertA("4")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame2, text="5", font=("tahoma", 12), command=lambda: insertA("5")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame2, text="6", font=("tahoma", 12), command=lambda: insertA("6")).pack(side=LEFT, expand=True, fill=BOTH)

#3
frame3 = Frame(root)
frame3.grid(row=3, column=0, columnspan=3, sticky="we")
Button(frame3, text="7", font=("tahoma", 12), command=lambda: insertA("7")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame3, text="8", font=("tahoma", 12), command=lambda: insertA("8")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame3, text="9", font=("tahoma", 12), command=lambda: insertA("9")).pack(side=LEFT, expand=True, fill=BOTH)

#4
frame4 = Frame(root)
frame4.grid(row=4, column=0, columnspan=3, sticky="we")
Button(frame4, text="-", font=("tahoma", 12), command=lambda: insertA("-")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame4, text="0", font=("tahoma", 12), command=lambda: insertA("0")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame4, text=".", font=("tahoma", 12), command=lambda: insertA(".")).pack(side=LEFT, expand=True, fill=BOTH)

#5
frame5 = Frame(root)
frame5.grid(row=5, column=0, columnspan=3, sticky="we")
Button(frame5, text="+", font=("tahoma", 12), command=lambda: insertA("+")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame5, text="-", font=("tahoma", 12), command=lambda: insertA("-")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame5, text="*", font=("tahoma", 12), command=lambda: insertA("*")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame5, text="/", font=("tahoma", 12), command=lambda: insertA("/")).pack(side=LEFT, expand=True, fill=BOTH)
Button(frame5, text="=", font=("tahoma", 12), command=tinh).pack(side=LEFT, expand=True, fill=BOTH)

#6
frame6 = Frame(root)
frame6.grid(row=6, column=0, columnspan=3, sticky="we")
Button(frame6, text="Clr", font=("tahoma", 12), command=delete).pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()