import csv
import random

FILE_NAME = "dulieu.csv"

# ------------------ 1. TẠO FILE CSV ------------------
def tao_file_csv():
    with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=';')
        for _ in range(10):  # 10 dòng
            dong = [random.randint(1, 100) for _ in range(10)]  # 10 số ngẫu nhiên
            writer.writerow(dong)
    print(f"Đã tạo file {FILE_NAME} với 10 dòng dữ liệu ngẫu nhiên.")

# ------------------ 2. ĐỌC FILE CSV & TÍNH TỔNG ------------------
def doc_file():
    try:
        with open(FILE_NAME, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=';')  
            for i, dong in enumerate(reader, start=1):
                print(f"{dong} ")
    except FileNotFoundError:
        print("Chưa có file dữ liệu. Hãy tạo file CSV trước.")

# ------------------ 3. MENU CHÍNH ------------------
def main():
    while True:
        print("\n=== XỬ LÝ CSV FILE ===")
        print("1. Tạo file CSV (10 dòng ngẫu nhiên)")
        print("2. Đọc file CSV và tính tổng")
        print("3. Thoát")
        chon = input("Chọn chức năng (1-3): ")

        match chon:
            case "1":
                tao_file_csv()
            case "2":
                doc_file()
            case "3":
                print("Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
