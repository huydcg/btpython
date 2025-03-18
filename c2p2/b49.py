def is_prime(n):
    # Kiểm tra nếu n nhỏ hơn hoặc bằng 1
    if n <= 1:
        return False
    # Kiểm tra các số từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Chương trình chính
def main():
    # Đọc số nguyên từ người dùng
    number = int(input("Nhập một số nguyên: "))

    # Kiểm tra và hiển thị kết quả
    if is_prime(number):
        print(f"Số {number} là số nguyên tố.")
    else:
        print(f"Số {number} không phải là số nguyên tố.")

# Gọi chương trình chính
if __name__ == "__main__":
    main()