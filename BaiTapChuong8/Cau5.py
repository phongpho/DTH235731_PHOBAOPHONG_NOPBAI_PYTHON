from tkinter import *
import json
import os

FILE_NAME = "password.json"

# ====== HÀM XỬ LÝ FILE ======
def doc_password():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data.get("password", "")
    return ""

def ghi_password(new_pw):
    with open(FILE_NAME, "w") as f:
        json.dump({"password": new_pw}, f)

# ====== HÀM KHI NHẤN NÚT ======
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

# ====== GIAO DIỆN ======
root = Tk()
root.title("Change Password")
root.geometry("400x200")

Label(root, text="Change Password", fg="blue", font=("tahoma", 14, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack()

Label(frame, text="Old password:", font=("tahoma", 11)).grid(row=0, column=0, sticky=W, padx=5, pady=5)
entry_old = Entry(frame, width=25, show="*", font=("tahoma", 11))
entry_old.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="New password:", font=("tahoma", 11)).grid(row=1, column=0, sticky=W, padx=5, pady=5)
entry_new = Entry(frame, width=25, show="*", font=("tahoma", 11))
entry_new.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Confirm password:", font=("tahoma", 11)).grid(row=2, column=0, sticky=W, padx=5, pady=5)
entry_confirm = Entry(frame, width=25, show="*", font=("tahoma", 11))
entry_confirm.grid(row=2, column=1, padx=5, pady=5)

frame_btn = Frame(root)
frame_btn.pack(pady=10)

Button(frame_btn, text="Enter", width=10, command=save_password).pack(side=LEFT, padx=10)
Button(frame_btn, text="Cancel", width=10, command=cancel).pack(side=LEFT, padx=10)

root.mainloop()
