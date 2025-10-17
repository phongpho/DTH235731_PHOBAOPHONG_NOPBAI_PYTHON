from tkinter import *
window =  Tk()
window.title('Demo Label')
Label(window,
    text= 'Lập trình Python.',
    justify= CENTER,
    relief=SUNKEN).pack(pady=10)
photo = PhotoImage(file='python.png')
Label(window, image=photo,
      relief=RAISED).pack(side=LEFT,padx=5)
window.resizable(height=True,width=True)
window.minsize(height=300, width=400)
window.mainloop()