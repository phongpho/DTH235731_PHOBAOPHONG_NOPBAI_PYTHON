from Cau1_XuLyFile import *

dssp = DocFile("database.txt")

def XuatSanPham(dssp):
    print("Danh sách sản phẩm:")
    for row in dssp:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
    print()

def SortSp(dssp):
    dssp.sort(key=lambda x: x[2], reverse=True)

XuatSanPham(dssp)

SortSp(dssp)
print("Danh sách sau khi sắp xếp theo đơn giá giảm dần:")
XuatSanPham(dssp)

