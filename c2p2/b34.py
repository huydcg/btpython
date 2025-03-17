# Đọc số thập phân từ người dùng
try:
    decimal_number = int(input("Nhập một số thập phân: "))

    # Chuyển đổi số thập phân thành nhị phân
    binary_number = bin(decimal_number)[2:]

    # Hiển thị kết quả
    print(f"Số thập phân {decimal_number} chuyển đổi thành nhị phân là: {binary_number}")

except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")