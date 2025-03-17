# Đọc tên của một tháng từ người dùng
thang = input("Nhập tên của một tháng: ").strip().lower()

# Xác định số ngày trong tháng
if thang in ["tháng 1", "january", "jan"]:
    so_ngay = 31
elif thang in ["tháng 2", "february", "feb"]:
    so_ngay = "28 hoặc 29"
elif thang in ["tháng 3", "march", "mar"]:
    so_ngay = 31
elif thang in ["tháng 4", "april", "apr"]:
    so_ngay = 30
elif thang in ["tháng 5", "may"]:
    so_ngay = 31
elif thang in ["tháng 6", "june", "jun"]:
    so_ngay = 30
elif thang in ["tháng 7", "july", "jul"]:
    so_ngay = 31
elif thang in ["tháng 8", "august", "aug"]:
    so_ngay = 31
elif thang in ["tháng 9", "september", "sep"]:
    so_ngay = 30
elif thang in ["tháng 10", "october", "oct"]:
    so_ngay = 31
elif thang in ["tháng 11", "november", "nov"]:
    so_ngay = 30
elif thang in ["tháng 12", "december", "dec"]:
    so_ngay = 31
else:
    so_ngay = None

# Hiển thị kết quả hoặc thông báo lỗi
if so_ngay:
    print(f"Số ngày trong {thang} là {so_ngay} ngày.")
else:
    print("Lỗi: Tên tháng không hợp lệ.")