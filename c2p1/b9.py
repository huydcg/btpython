from math import pi, sin, sqrt
print("Goi tam giac ABC bat ky:")
a = float(input("Nhap canh a cua tam giac (AB): ")) #6
b = float(input("Nhap canh b cua tam giac (BC): ")) #6
c = float(input("Nhap canh c cua tam giac (CA): ")) #6

A = float(input("Nhap goc A (BAC) cua tam giac (radian): ")) # 2.0944

S1 = 0.5 * a * b * sin(A)
S2 = 0.5 * b * c * sin(A)
S3 = 0.5 * c * a * sin(A)
print("Dien tich tam giac:" + str(round(S1, 2)))
print("Dien tich tam giac:" + str(round(S2, 2)))
print("Dien tich tam giac:" + str(round(S3, 2)))


