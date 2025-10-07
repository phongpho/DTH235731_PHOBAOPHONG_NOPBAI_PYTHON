import json
import os

FILE_NAME = "sinhvien.json"

# ---------------------- LỚP ĐỐI TƯỢNG ----------------------
class SinhVien:
    def __init__(self, ma_sv, ten_sv, nam_sinh):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.nam_sinh = int(nam_sinh)

class Lop:
    def __init__(self, ma_lop, ten_lop):
        self.ma_lop = ma_lop
        self.ten_lop = ten_lop
        self.sinh_vien = []  # danh sách sinh viên thuộc lớp

# ---------------------- XỬ LÝ FILE JSON ----------------------
def doc_file():
    ds_lop = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            for ma_lop, info in data.items():
                lop = Lop(ma_lop, info["ten_lop"])
                for sv in info["sinh_vien"]:
                    lop.sinh_vien.append(SinhVien(sv["ma_sv"], sv["ten_sv"], sv["nam_sinh"]))
                ds_lop[ma_lop] = lop
    return ds_lop

def ghi_file(ds_lop):
    data = {}
    for ma_lop, lop in ds_lop.items():
        data[ma_lop] = {
            "ten_lop": lop.ten_lop,
            "sinh_vien": [
                {"ma_sv": sv.ma_sv, "ten_sv": sv.ten_sv, "nam_sinh": sv.nam_sinh}
                for sv in lop.sinh_vien
            ]
        }
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Đã lưu dữ liệu vào file sinhvien.json")

# ---------------------- CÁC CHỨC NĂNG ----------------------
def hien_thi(ds_lop):
    if not ds_lop:
        print("Chưa có dữ liệu.")
        return
    for lop in ds_lop.values():
        print(f"\nLớp: {lop.ma_lop} - {lop.ten_lop}")
        if not lop.sinh_vien:
            print("  (Không có sinh viên)")
        else:
            print("{:<10}{:<20}{:<10}".format("Mã SV", "Tên sinh viên", "Năm sinh"))
            for sv in lop.sinh_vien:
                print("{:<10}{:<20}{:<10}".format(sv.ma_sv, sv.ten_sv, sv.nam_sinh))

def them_sinh_vien(ds_lop):
    ma_lop = input("Nhập mã lớp: ").strip()
    ten_lop = input("Nhập tên lớp: ").strip()
    if ma_lop not in ds_lop:
        ds_lop[ma_lop] = Lop(ma_lop, ten_lop)
    else:
        ds_lop[ma_lop].ten_lop = ten_lop

    ma_sv = input("Nhập mã sinh viên: ").strip()
    # kiểm tra trùng mã
    for lop in ds_lop.values():
        for sv in lop.sinh_vien:
            if sv.ma_sv == ma_sv:
                print("Mã sinh viên đã tồn tại!")
                return
    ten_sv = input("Nhập tên sinh viên: ").strip()
    try:
        nam_sinh = int(input("Nhập năm sinh: "))
    except:
        print("Năm sinh không hợp lệ!")
        return
    ds_lop[ma_lop].sinh_vien.append(SinhVien(ma_sv, ten_sv, nam_sinh))
    print("Đã thêm sinh viên thành công.")

def sua_sinh_vien(ds_lop):
    ma_sv = input("Nhập mã sinh viên cần sửa: ").strip()
    for lop in ds_lop.values():
        for sv in lop.sinh_vien:
            if sv.ma_sv == ma_sv:
                sv.ten_sv = input(f"Tên mới ({sv.ten_sv}): ") or sv.ten_sv
                nam = input(f"Năm sinh mới ({sv.nam_sinh}): ")
                if nam:
                    sv.nam_sinh = int(nam)
                print("Đã cập nhật thông tin sinh viên.")
                return
    print("Không tìm thấy sinh viên!")

def xoa_sinh_vien(ds_lop):
    ma_sv = input("Nhập mã sinh viên cần xóa: ").strip()
    for lop in ds_lop.values():
        for sv in lop.sinh_vien:
            if sv.ma_sv == ma_sv:
                lop.sinh_vien.remove(sv)
                print("Đã xóa sinh viên.")
                return
    print("Không tìm thấy sinh viên!")

def tim_kiem(ds_lop):
    tu_khoa = input("Nhập tên sinh viên cần tìm: ").lower()
    ket_qua = []
    for lop in ds_lop.values():
        for sv in lop.sinh_vien:
            if tu_khoa in sv.ten_sv.lower():
                ket_qua.append((lop, sv))
    if not ket_qua:
        print("Không tìm thấy sinh viên.")
    else:
        print("\nKết quả tìm kiếm:")
        for lop, sv in ket_qua:
            print(f"{sv.ma_sv} - {sv.ten_sv} ({sv.nam_sinh}) thuộc lớp {lop.ten_lop}")

def sap_xep(ds_lop):
    print("1. Theo tên sinh viên")
    print("2. Theo năm sinh (tăng dần)")
    chon = input("Chọn kiểu sắp xếp: ")
    for lop in ds_lop.values():
        if chon == "1":
            lop.sinh_vien.sort(key=lambda sv: sv.ten_sv.lower())
        elif chon == "2":
            lop.sinh_vien.sort(key=lambda sv: sv.nam_sinh)
    print("Đã sắp xếp xong.")

# ---------------------- MENU CHÍNH ----------------------
def main():
    ds_lop = doc_file()
    while True:
        print("\n=== QUẢN LÝ SINH VIÊN ===")
        print("1. Xem danh sách")
        print("2. Thêm sinh viên")
        print("3. Sửa sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm")
        print("6. Sắp xếp")
        print("7. Lưu file JSON")
        print("8. Thoát")
        chon = input("Chọn chức năng (1-8): ")

        match chon:
            case "1":
                hien_thi(ds_lop)
            case "2":
                them_sinh_vien(ds_lop)
            case "3":
                sua_sinh_vien(ds_lop)
            case "4":
                xoa_sinh_vien(ds_lop)
            case "5":
                tim_kiem(ds_lop)
            case "6":
                sap_xep(ds_lop)
            case "7":
                ghi_file(ds_lop)
            case "8":
                print("Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
