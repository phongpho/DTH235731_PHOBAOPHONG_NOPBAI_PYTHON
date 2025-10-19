from tkinter import *

window = Tk()
window.title('Lập trình Tkinter')
window.geometry('350x200')
lbl = Label(window, text='Hello')
lbl.grid(column=0,row=0)

txt = Entry(window, width= 10)
txt .grid(column=1,row=0)

txt.focus()

def clicked():
    res = 'Welcome to '+txt.get()
    lbl.configure(text=res)

btn = Button(window, text='Clicked Me', command=clicked)
btn.grid(column=2,row=0)

window.mainloop()