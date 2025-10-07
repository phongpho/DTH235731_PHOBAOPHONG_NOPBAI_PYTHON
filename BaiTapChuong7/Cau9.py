import os

FILE_NAME = "sanpham.txt"

class SanPham:
    def __init__(self, ma_sp, ten_sp, don_gia):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.don_gia = float(don_gia)

class DanhMuc:
    def __init__(self, ma_dm, ten_dm):
        self.ma_dm = ma_dm
        self.ten_dm = ten_dm
        self.san_pham = []  # danh sách sản phẩm thuộc danh mục này

# ---------- XỬ LÝ FILE ----------
def doc_file():
    ds_dm = {}
    if not os.path.exists(FILE_NAME):
        return ds_dm

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == "": 
                continue
            ma_dm, ten_dm, ma_sp, ten_sp, gia = line.strip().split(";")
            if ma_dm not in ds_dm:
                ds_dm[ma_dm] = DanhMuc(ma_dm, ten_dm)
            ds_dm[ma_dm].san_pham.append(SanPham(ma_sp, ten_sp, gia))
    return ds_dm

def ghi_file(ds_dm):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for dm in ds_dm.values():
            for sp in dm.san_pham:
                f.write(f"{dm.ma_dm};{dm.ten_dm};{sp.ma_sp};{sp.ten_sp};{sp.don_gia}\n")
    print("✅ Đã lưu dữ liệu vào file sanpham.txt")

# ---------- CÁC CHỨC NĂNG ----------
def hien_thi(ds_dm):
    if not ds_dm:
        print("❗ Chưa có danh mục hoặc sản phẩm.")
        return
    for dm in ds_dm.values():
        print(f"\n📂 Danh mục: {dm.ma_dm} - {dm.ten_dm}")
        if not dm.san_pham:
            print("  (Không có sản phẩm)")
        else:
            print("{:<10}{:<20}{:<10}".format("Mã SP", "Tên sản phẩm", "Đơn giá"))
            for sp in dm.san_pham:
                print("{:<10}{:<20}{:<10}".format(sp.ma_sp, sp.ten_sp, sp.don_gia))

def them_san_pham(ds_dm):
    ma_dm = input("Nhập mã danh mục: ")
    ten_dm = input("Nhập tên danh mục: ")

    if ma_dm not in ds_dm:
        ds_dm[ma_dm] = DanhMuc(ma_dm, ten_dm)

    ma_sp = input("Nhập mã sản phẩm: ")
    ten_sp = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập đơn giá: "))
    ds_dm[ma_dm].san_pham.append(SanPham(ma_sp, ten_sp, gia))
    print("Đã thêm sản phẩm.")

def sua_san_pham(ds_dm):
    ma_sp = input("Nhập mã sản phẩm cần sửa: ")
    for dm in ds_dm.values():
        for sp in dm.san_pham:
            if sp.ma_sp == ma_sp:
                sp.ten_sp = input(f"Tên mới ({sp.ten_sp}): ") or sp.ten_sp
                gia = input(f"Giá mới ({sp.don_gia}): ")
                if gia: sp.don_gia = float(gia)
                print("✅ Đã cập nhật sản phẩm.")
                return
    print("Không tìm thấy sản phẩm.")

def xoa_san_pham(ds_dm):
    ma_sp = input("Nhập mã sản phẩm cần xóa: ")
    for dm in ds_dm.values():
        for sp in dm.san_pham:
            if sp.ma_sp == ma_sp:
                dm.san_pham.remove(sp)
                print("✅ Đã xóa sản phẩm.")
                return
    print("Không tìm thấy sản phẩm.")

def tim_kiem(ds_dm):
    tu_khoa = input("Nhập tên sản phẩm cần tìm: ").lower()
    ket_qua = []
    for dm in ds_dm.values():
        for sp in dm.san_pham:
            if tu_khoa in sp.ten_sp.lower():
                ket_qua.append((dm, sp))
    if not ket_qua:
        print("Không tìm thấy sản phẩm phù hợp.")
    else:
        print("\nKết quả tìm kiếm:")
        for dm, sp in ket_qua:
            print(f"{sp.ma_sp} - {sp.ten_sp} - {sp.don_gia} ({dm.ten_dm})")

def sap_xep(ds_dm):
    print("1. Theo tên sản phẩm")
    print("2. Theo giá tăng dần")
    chon = input("Chọn kiểu sắp xếp: ")
    for dm in ds_dm.values():
        if chon == "1":
            dm.san_pham.sort(key=lambda sp: sp.ten_sp)
        elif chon == "2":
            dm.san_pham.sort(key=lambda sp: sp.don_gia)
    print("✅Đã sắp xếp xong.")

# ---------- MENU CHÍNH ----------
def main():
    ds_dm = doc_file()
    while True:
        print("\n=== QUẢN LÝ SẢN PHẨM ===")
        print("1. Xem danh sách")
        print("2. Thêm sản phẩm")
        print("3. Sửa sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm")
        print("6. Sắp xếp")
        print("7. Lưu file")
        print("8. Thoát")
        chon = input("Chọn chức năng (1-8): ")
        match chon:
            case "1":
                hien_thi(ds_dm)
            case "2":
                them_san_pham(ds_dm)
            case "3":
                sua_san_pham(ds_dm)
            case "4":
                xoa_san_pham(ds_dm)
            case "5":
                tim_kiem(ds_dm)
            case "6":
                sap_xep(ds_dm)
            case "7":
                ghi_file(ds_dm)
            case "8":
                print("Tạm biệt 👋")
                break
            case _:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
