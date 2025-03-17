# Đọc độ dài ba cạnh của tam giác từ người dùng
try:
    a = float(input("Nhập độ dài cạnh thứ nhất: "))
    b = float(input("Nhập độ dài cạnh thứ hai: "))
    c = float(input("Nhập độ dài cạnh thứ ba: "))

    # Kiểm tra xem ba cạnh có tạo thành một tam giác hay không
    if a + b > c and a + c > b and b + c > a:
        # Xác định loại tam giác
        if a == b == c:
            loai_tam_giac = "tam giác đều"
        elif a == b or a == c or b == c:
            loai_tam_giac = "tam giác cân"
        else:
            loai_tam_giac = "tam giác thường"
        
        # Hiển thị loại tam giác
        print(f"Tam giác với các cạnh {a}, {b}, {c} là {loai_tam_giac}.")
    else:
        print("Ba cạnh đã nhập không tạo thành một tam giác hợp lệ.")

except ValueError:
    print("Lỗi: Vui lòng nhập một số hợp lệ.")