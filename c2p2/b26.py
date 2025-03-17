# Đọc một chữ cái từ người dùng
chu_cai = input("Nhập một chữ cái: ").lower()

# Kiểm tra và hiển thị thông báo tương ứng
if chu_cai in ['a', 'e', 'i', 'o', 'u']:
    print(f"Chữ cái '{chu_cai}' là nguyên âm.")
elif chu_cai == 'y':
    print(f"Chữ cái '{chu_cai}' có thể là nguyên âm hoặc phụ âm.")
else:
    print(f"Chữ cái '{chu_cai}' là phụ âm.")