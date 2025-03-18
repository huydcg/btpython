def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Đọc số nguyên từ người dùng
number = int(input("Nhập một số nguyên: "))

# Tính giai thừa của số cho trước
result = factorial(number)

# In kết quả
print(f"Giai thừa của {number} là: {result}")