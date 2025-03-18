def calculate_average(a, b, c):
    # Tính giá trị trung bình của ba tham số
    return (a + b + c) / 3

# Chương trình chính
def main():
    # Đọc ba giá trị từ người dùng
    value1 = float(input("Nhập giá trị thứ nhất: "))
    value2 = float(input("Nhập giá trị thứ hai: "))
    value3 = float(input("Nhập giá trị thứ ba: "))

    # Tính giá trị trung bình
    average = calculate_average(value1, value2, value3)

    # Hiển thị giá trị trung bình
    print(f"Giá trị trung bình của {value1}, {value2}, và {value3} là: {average}")

# Gọi chương trình chính
if __name__ == "__main__":
    main()