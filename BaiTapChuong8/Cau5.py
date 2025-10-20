from tkinter import *
import json
import os

FILE_NAME = "password.json"


def doc_password():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data.get("password", "")
    return ""

def ghi_password(new_pw):
    with open(FILE_NAME, "w") as f:
        json.dump({"password": new_pw}, f)


def save_password():
    old_pw = entry_old.get()
    new_pw = entry_new.get()
    confirm_pw = entry_confirm.get()
    current_pw = doc_password()

    if old_pw == current_pw or current_pw == "":
        if new_pw == confirm_pw:
            ghi_password(new_pw)
            entry_old.delete(0, END)
            entry_new.delete(0, END)
            entry_confirm.delete(0, END)

def cancel():
    root.destroy()

root = Tk()
root.title("Enter New Password")
root.minsize(height=100, width=200)
root.resizable(height=True, width=True)

frame = Frame(root)
frame.grid(row=0, column=0, columnspan=2)

Label(frame, text="Old password:", font=("tahoma", 11)).grid(row=0, column=0, sticky=W)
entry_old = Entry(frame, width=25, show="*", font=("tahoma", 11))
entry_old.grid(row=0, column=1)

Label(frame, text="New password:", font=("tahoma", 11)).grid(row=1, column=0, sticky=W)
entry_new = Entry(frame, width=25, show="*", font=("tahoma", 11))
entry_new.grid(row=1, column=1)

Label(frame, text="Enter New Password Again:", font=("tahoma", 11)).grid(row=2, column=0, sticky=W)
entry_confirm = Entry(frame, width=25, show="*", font=("tahoma", 11))
entry_confirm.grid(row=2, column=1)

frame_btn = Frame(root)
frame_btn.grid(row=3, columnspan= 2, pady= 10)

Button(frame_btn, text="Ok", width=10, command=save_password).pack(side=LEFT,padx= 5)
Button(frame_btn, text="Cancel", width=10, command=cancel).pack(side=LEFT, padx=5)

root.mainloop()
