from math import pi, sin, sqrt
print("Goi tam giac ABC bat ky:")
a = float(input("Nhap canh a cua tam giac (AB): ")) #6
b = float(input("Nhap canh b cua tam giac (BC): ")) #7
c = float(input("Nhap canh c cua tam giac (CA): ")) #8

A = float(input("Nhap goc A (BAC) cua tam giac (radian): ")) # 1.01
B = float(input("Nhap goc B (ABC) cua tam giac (radian): ")) # 1.32
C = float(input("Nhap goc C (BCA) cua tam giac (radian): ")) # 0.81

S1 = 0.5 * a * b * sin(B)
S2 = 0.5 * b * c * sin(C)
S3 = 0.5 * c * a * sin(A)
print("Dien tich tam giac:" + str(round(S1, 2)))
print("Dien tich tam giac:" + str(round(S2, 2)))
print("Dien tich tam giac:" + str(round(S3, 2)))


