def is_perfect_number(n):
    # Kiểm tra nếu n nhỏ hơn hoặc bằng 1
    if n <= 1:
        return False
    
    # Tính tổng các ước số của n
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    
    # Kiểm tra nếu tổng các ước số bằng n
    return sum_of_divisors == n

# Chương trình chính
def main():
    # Đọc số nguyên dương từ người dùng
    number = int(input("Nhập một số nguyên dương: "))
    
    # Kiểm tra và hiển thị kết quả
    if is_perfect_number(number):
        print(f"Số {number} là số hoàn hảo.")
    else:
        print(f"Số {number} không phải là số hoàn hảo.")

# Gọi chương trình chính
if __name__ == "__main__":
    main()