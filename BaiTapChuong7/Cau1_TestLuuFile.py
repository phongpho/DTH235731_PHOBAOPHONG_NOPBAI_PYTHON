from Cau1_XuLyFile import *

masp = input("Nhập mã SP: ")
tensp = input("Nhập tên SP: ")
dongia = float(input("Nhập đơn giá: "))

line = f"{masp};{tensp};{dongia}"
LuuFile("database.txt", line)

print("Sản phẩm đã được lưu vào file.")
