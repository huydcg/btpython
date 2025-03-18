import random

def generate_random_password():
    # Độ dài ngẫu nhiên từ 7 đến 10 ký tự
    length = random.randint(7, 10)
    
    # Tạo mật khẩu ngẫu nhiên
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    
    return password

# Chương trình chính
def main():
    # Tạo mật khẩu ngẫu nhiên
    random_password = generate_random_password()
    
    # Hiển thị mật khẩu được tạo ngẫu nhiên
    print("Mật khẩu ngẫu nhiên được tạo:", random_password)

# Gọi chương trình chính
if __name__ == "__main__":
    main()