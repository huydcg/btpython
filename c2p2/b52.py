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
    # Xác định và hiển thị tất cả các số hoàn hảo trong khoảng từ 1 đến 10.000
    print("Các số hoàn hảo trong khoảng từ 1 đến 10.000 là:")
    for number in range(1, 10001):
        if is_perfect_number(number):
            print(number)

# Gọi chương trình chính
if __name__ == "__main__":
    main()