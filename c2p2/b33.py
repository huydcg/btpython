# Đọc một chuỗi từ người dùng
chuoi = input("Nhập một chuỗi: ").strip()

# Hàm kiểm tra Palindrome
def is_palindrome(s):
    # Loại bỏ khoảng trắng và chuyển đổi thành chữ thường
    s = s.replace(" ", "").lower()
    # Sử dụng vòng lặp để kiểm tra đối xứng
    for i in range(len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True

# Kiểm tra và hiển thị kết quả
if is_palindrome(chuoi):
    print(f"Chuỗi '{chuoi}' là một Palindrome.")
else:
    print(f"Chuỗi '{chuoi}' không phải là một Palindrome.")