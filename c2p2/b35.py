# Đọc các số từ người dùng, ngăn cách bởi dấu phẩy
input_numbers = input("Nhập các số, ngăn cách bởi dấu phẩy: ")

# Chuyển đổi chuỗi đầu vào thành danh sách các số nguyên
numbers = [int(num) for num in input_numbers.split(",")]

# Tạo danh sách các số lẻ
odd_numbers = [num for num in numbers if num % 2 != 0]

# Hiển thị kết quả
print("Danh sách các số lẻ là:", odd_numbers)