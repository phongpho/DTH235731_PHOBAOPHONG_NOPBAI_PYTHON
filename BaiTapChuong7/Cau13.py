import xml.etree.ElementTree as ET
from collections import defaultdict

# ---------------------- Đọc file nhóm ----------------------
def doc_nhom(file_nhom):
    nhoms = {}
    try:
        tree = ET.parse(file_nhom)
        root = tree.getroot()
        for nhom in root.findall("nhom"):
            ma = nhom.find("ma").text.strip()
            ten = nhom.find("ten").text.strip()
            nhoms[ma] = ten
        return nhoms
    except FileNotFoundError:
        print("Không tìm thấy file nhóm thiết bị.")
        return {}

# ---------------------- Đọc file thiết bị ----------------------
def doc_thietbi(file_tb):
    thietbis = []
    try:
        tree = ET.parse(file_tb)
        root = tree.getroot()
        for tb in root.findall("thietbi"):
            manhom = tb.get("manhom")
            ma = tb.find("ma").text.strip()
            ten = tb.find("ten").text.strip()
            thietbis.append({"ma": ma, "ten": ten, "manhom": manhom})
        return thietbis
    except FileNotFoundError:
        print("Không tìm thấy file thiết bị.")
        return []

# ---------------------- Hiển thị danh sách ----------------------
def hien_thi_nhom(nhoms):
    print("\n=== DANH SÁCH NHÓM THIẾT BỊ ===")
    for ma, ten in nhoms.items():
        print(f"{ma} - {ten}")

def hien_thi_thietbi(thietbis):
    print("\n=== DANH SÁCH THIẾT BỊ ===")
    for tb in thietbis:
        print(f"{tb['ma']} - {tb['ten']} (Nhóm: {tb['manhom']})")

# ---------------------- Lọc thiết bị theo nhóm ----------------------
def loc_theo_nhom(thietbis, ma_nhom):
    kq = [tb for tb in thietbis if tb["manhom"] == ma_nhom]
    if not kq:
        print("Không có thiết bị thuộc nhóm này.")
    else:
        print(f"\nThiết bị thuộc nhóm {ma_nhom}:")
        for tb in kq:
            print(f"{tb['ma']} - {tb['ten']}")

# ---------------------- Nhóm có nhiều thiết bị nhất ----------------------
def nhom_nhieu_tb_nhat(thietbis, nhoms):
    dem = defaultdict(int)
    for tb in thietbis:
        dem[tb["manhom"]] += 1
    if not dem:
        print("Không có dữ liệu thiết bị.")
        return
    max_count = max(dem.values())
    print("\nNhóm có nhiều thiết bị nhất:")
    for ma_nhom, sl in dem.items():
        if sl == max_count:
            print(f"{nhoms.get(ma_nhom, ma_nhom)} ({ma_nhom}) - {sl} thiết bị")

# ---------------------- MENU CHÍNH ----------------------
def main():
    file_nhom = "nhomthietbi.xml"
    file_tb = "ThietBi.xml"

    nhoms = doc_nhom(file_nhom)
    thietbis = doc_thietbi(file_tb)

    while True:
        print("\n=== QUẢN LÝ THIẾT BỊ (XML) ===")
        print("1. Hiển thị danh sách nhóm thiết bị")
        print("2. Hiển thị toàn bộ thiết bị")
        print("3. Lọc thiết bị theo mã nhóm")
        print("4. Xuất nhóm có nhiều thiết bị nhất")
        print("5. Thoát")
        chon = input("Chọn chức năng (1-5): ")

        match chon:
            case "1":
                hien_thi_nhom(nhoms)
            case "2":
                hien_thi_thietbi(thietbis)
            case "3":
                ma = input("Nhập mã nhóm cần lọc: ").strip()
                loc_theo_nhom(thietbis, ma)
            case "4":
                nhom_nhieu_tb_nhat(thietbis, nhoms)
            case "5":
                print("Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
