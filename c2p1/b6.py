from math import pi

r = float(input("Nhap ban kinh mat day hinh tru: "))
h = float(input("Nhap chieu cao hinh tru: "))
v = pi * r ** 2 * h
print(f"The tich hinh tru: {v:.2f}")
print("The tich hinh tru: " + str(round(v, 2)))