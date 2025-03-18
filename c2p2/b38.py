# Tạo danh sách để lưu trữ các số nguyên
numbers = []

# Đọc các số nguyên từ người dùng cho đến khi nhập vào một dòng trống
while True:
    input_value = input("Nhập một số nguyên (nhập dòng trống để kết thúc): ").strip()
    if input_value == "":
        break
    try:
        num = int(input_value)
        numbers.append(num)
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

# Tạo các danh sách riêng biệt cho số âm, số không và số dương
negative_numbers = [num for num in numbers if num < 0]
zero_numbers = [num for num in numbers if num == 0]
positive_numbers = [num for num in numbers if num > 0]

# Hiển thị các số theo quy tắc đã cho
print("Các số đã nhập theo quy tắc:")
for num in negative_numbers + zero_numbers + positive_numbers:
    print(num)