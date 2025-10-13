from tkinter import *

root = Tk()
root.title("frame 2")

frame = Frame(root)
frame.pack(padx=10, pady=10)

styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

for i in range(5):
    Label(frame, text=f"borderwidth = {i}", width=15, anchor=W).grid(row=i, column=0, padx=5, pady=5)
    for j, style in enumerate(styles):
        Button(frame, text=style, relief=style, borderwidth=i, width=8).grid(row=i, column=j+1, padx=5, pady=5)

root.mainloop()
