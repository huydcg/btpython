# Tạo danh sách để lưu trữ các số nguyên
numbers = []

# Đọc các số nguyên từ người dùng cho đến khi nhập 0
while True:
    num = int(input("Nhập một số nguyên (nhập 0 để kết thúc): "))
    if num == 0:
        break
    numbers.append(num)

# Sắp xếp danh sách theo thứ tự tăng dần
numbers.sort()

# Hiển thị các giá trị theo thứ tự tăng dần, mỗi giá trị trên một dòng
print("Các giá trị đã nhập theo thứ tự tăng dần:")
for num in numbers:
    print(num)