def create_and_print_squares():
    # Tạo danh sách để lưu trữ các giá trị bình phương
    squares = []
    
    # Sử dụng range() cho vòng lặp từ 1 đến 20
    for i in range(1, 21):
        # Sử dụng toán tử ** để lấy giá trị bình phương và thêm vào danh sách
        squares.append(i ** 2)
    
    # In danh sách các giá trị bình phương
    print(squares)

# Gọi hàm để tạo và in danh sách các giá trị bình phương
create_and_print_squares()