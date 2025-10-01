from tkinter import *
parent = Tk()
name = Label (parent, text = 'Name').grid(row = 0, column = 0)
e1 = Entry(parent).grid(row = 0, column = 1)

password = Label(parent, text = 'Password').grid(row = 1, column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)

submit = Button(parent, text = 'Submit').grid(row = 4, column = 0)

def makecenter(root):
    root.update_idletask()
    Width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth()//2) - (Width//2)
    y = (root.winfo_screenheight()//2) - (height//2)
    root.geometry('{}x{}+{}+{}'.format(Width, height,x,y))
makecenter(parent)

parent.mainloop()
