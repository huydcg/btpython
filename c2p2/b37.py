# Tạo danh sách để lưu trữ các từ
words = []

# Đọc các từ từ người dùng cho đến khi nhập vào một dòng trống
while True:
    word = input("Nhập một từ (nhập dòng trống để kết thúc): ").strip()
    if word == "":
        break
    if word not in words:
        words.append(word)

# Hiển thị các từ đã nhập sau khi loại bỏ từ bị trùng
print("Các từ đã nhập:")
for word in words:
    print(word)