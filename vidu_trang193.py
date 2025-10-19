from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Lập trình Tkinter')
window.geometry('350x200')
lbl = Label(window, text='Hello')
lbl.grid(column=0,row=0)

def clicked():
    messagebox.showinfo('Message tittle', 'Message content')

btn = Button(window, text='Clicked Me', command=clicked)
btn.grid(column=1,row=0)
window.mainloop()