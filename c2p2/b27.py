# Đọc số cạnh từ người dùng
so_canh = int(input("Nhập số cạnh của hình dạng (từ 3 đến 10): "))

# Xác định tên của hình dạng dựa trên số cạnh
if so_canh == 3:
    hinh_dang = "hình tam giác"
elif so_canh == 4:
    hinh_dang = "hình tứ giác"
elif so_canh == 5:
    hinh_dang = "hình ngũ giác"
elif so_canh == 6:
    hinh_dang = "hình lục giác"
elif so_canh == 7:
    hinh_dang = "hình thất giác"
elif so_canh == 8:
    hinh_dang = "hình bát giác"
elif so_canh == 9:
    hinh_dang = "hình cửu giác"
elif so_canh == 10:
    hinh_dang = "hình thập giác"
else:
    hinh_dang = None

# Hiển thị kết quả hoặc thông báo lỗi
if hinh_dang:
    print(f"Số cạnh {so_canh} là {hinh_dang}.")
else:
    print("Lỗi: Chương trình chỉ hỗ trợ các hình dạng từ 3 đến 10 cạnh.")