# Đọc năm từ người dùng
try:
    nam = int(input("Nhập một năm: "))

    # Kiểm tra xem năm có phải là năm nhuận hay không
    if (nam % 400 == 0) or (nam % 100 != 0 and nam % 4 == 0):
        print(f"Năm {nam} là năm nhuận.")
    else:
        print(f"Năm {nam} không phải là năm nhuận.")

except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")