width = float(input("Nhập chiều rộng căn phòng: "))
length = float(input("Nhập chiều dài căn phòng: "))

# Tính diện tích căn phòng
area = width * length

truoc_phay = str(area).split('.')[0]
sau_phay = str(area).split('.')[1]

print(f"Diện tích căn phòng là: " + truoc_phay + "," + sau_phay)
