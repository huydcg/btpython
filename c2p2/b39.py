# Đọc số nguyên n từ người dùng
n = int(input("Nhập một số nguyên n: "))

# Tạo dictionary chứa các cặp (i, i*i)
result = {i: i*i for i in range(1, n+1)}

# In ra dictionary
print(result)