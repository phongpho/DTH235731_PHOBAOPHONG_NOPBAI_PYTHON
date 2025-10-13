from tkinter import *

def chuyen_F_sang_C():
    try:
        do_F = float(entry_F.get())  
        do_C = (do_F - 32) * 5 / 9   
        ket_qua.set(f"{round(do_C, 2)} °C")  
    except:
        ket_qua.set("Lỗi dữ liệu!")

root = Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("300x150")
root.configure(bg="white")

frame = Frame(root, bg="yellow", bd=2, relief="solid")
frame.pack(padx=0, pady=0, fill="both", expand=True)

Label(frame, text="Nhập độ F:", bg="yellow", font=("tahoma", 12)).grid(row=0, column=0, padx=5, pady=10, sticky=E)
entry_F = Entry(frame, width=15, font=("tahoma", 14), fg="red", justify="center")
entry_F.grid(row=0, column=1, padx=5, pady=10)

Button(frame, text="Chuyển", bg="steelblue", fg="white", font=("tahoma", 11, "bold"), width=10, command=chuyen_F_sang_C).grid(row=1, column=1, pady=5)

Label(frame, text="Độ C:", bg="yellow", font=("tahoma", 12)).grid(row=2, column=0, padx=5, pady=10, sticky=W)
ket_qua = StringVar()
Label(frame, textvariable=ket_qua, bg="yellow", font=("tahoma", 12, "bold")).grid(row=2, column=1, padx=5, pady=10, sticky=W)

root.mainloop()
