from tkinter import *

def tinh_BMI():
    try:
        cao = float(entry_cao.get()) / 100   
        nang = float(entry_nang.get())
        bmi = nang / (cao * cao)
        ketqua_BMI.set(round(bmi, 2))

        # Xác định tình trạng
        if bmi < 18.5:
            tinh_trang.set("Gầy")
            nguy_co.set("Thấp")
        elif bmi < 25:
            tinh_trang.set("Bình thường")
            nguy_co.set("Trung bình")
        elif bmi < 30:
            tinh_trang.set("Hơi béo")
            nguy_co.set("Hơi cao")
        else:
            tinh_trang.set("Béo phì")
            nguy_co.set("Rất cao")

    except:
        ketqua_BMI.set("Lỗi dữ liệu")
        tinh_trang.set("")
        nguy_co.set("")

root = Tk()
root.title("Tính chỉ số BMI")
root.geometry("400x350")
root.configure(bg="white")

frame = Frame(root, bg="yellow", bd=2, relief="solid")
frame.pack(padx=0, pady=0, fill="both", expand=True)

Label(frame, text="Nhập chiều cao:", bg="yellow", font=("tahoma", 12)).grid(row=0, column=0, padx=5, pady=10, sticky=W)
entry_cao = Entry(frame, width=15, font=("tahoma", 14), fg="red", justify="center")
entry_cao.grid(row=0, column=1, padx=5, pady=10)

Label(frame, text="Nhập cân nặng:", bg="yellow", font=("tahoma", 12)).grid(row=1, column=0, padx=5, pady=10, sticky=W)
entry_nang = Entry(frame, width=15, font=("tahoma", 14), fg="red", justify="center")
entry_nang.grid(row=1, column=1, padx=5, pady=10)

Button(frame, text="Tính BMI", bg="steelblue", fg="white", font=("tahoma", 11, "bold"), width=10,
       command=tinh_BMI).grid(row=2, column=1, pady=5)

Label(frame, text="BMI của bạn:", bg="yellow", font=("tahoma", 12)).grid(row=3, column=0, padx=5, pady=10, sticky=W)
ketqua_BMI = StringVar()
Entry(frame, textvariable=ketqua_BMI, font=("tahoma", 12, "bold"),
      width=15, justify="center", state="readonly").grid(row=3, column=1, padx=5, pady=10)

Label(frame, text="Tình trạng của bạn:", bg="yellow", font=("tahoma", 12)).grid(row=4, column=0, padx=5, pady=10, sticky=W)
tinh_trang = StringVar()
Entry(frame, textvariable=tinh_trang, font=("tahoma", 12, "bold"),
      width=15, justify="center", state="readonly").grid(row=4, column=1, padx=5, pady=10)

Label(frame, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("tahoma", 12)).grid(row=5, column=0, padx=5, pady=10, sticky=W)
nguy_co = StringVar()
Entry(frame, textvariable=nguy_co, font=("tahoma", 12, "bold"),
      width=15, justify="center", state="readonly").grid(row=5, column=1, padx=5, pady=10)

Button(frame, text="Thoát", bg="steelblue", fg="white", font=("tahoma", 11, "bold"), width=10, command=root.quit).grid(row=6, column=1, pady=10)

root.mainloop()
