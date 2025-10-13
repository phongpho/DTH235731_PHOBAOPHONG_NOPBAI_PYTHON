from tkinter import *

def chuyen_nam():
    try:
        nam = int(entry_nam.get())

        can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
        chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

        nam_am = can[nam % 10] + " " + chi[nam % 12]
        ket_qua.set(nam_am)
    except:
        ket_qua.set("Lỗi dữ liệu!")


root = Tk()
root.title("Chuyển năm Dương Lịch thành Âm Lịch")
root.geometry("400x220")
root.configure(bg="white")

frame = Frame(root, bg="yellow", bd=2, relief="solid")
frame.pack(padx=0, pady=0, fill="both", expand=True)

Label(frame, text="Nhập năm dương:", bg="yellow", font=("tahoma", 12)).grid(row=0, column=0, padx=5, pady=10, sticky=E)

entry_nam = Entry(frame, width=15, font=("tahoma", 14), fg="red", justify="center")
entry_nam.grid(row=0, column=1, padx=5, pady=10)


Button(frame, text="Chuyển", bg="steelblue", fg="white", font=("tahoma", 11, "bold"),
       width=10, command=chuyen_nam).grid(row=1, column=1, pady=5)


Label(frame, text="Năm âm:", bg="yellow", font=("tahoma", 12)).grid(row=2, column=0, padx=5, pady=10, sticky=W)

ket_qua = StringVar()
Label(frame, textvariable=ket_qua, bg="yellow", font=("tahoma", 12, "bold")).grid(row=2, column=1, padx=5, pady=10, sticky=W)

root.mainloop()
