n1 = float(input("Nhap so thu nhat:"))
n2 = float(input("Nhap so thu hai:"))
n3 = float(input("Nhap so thu ba:"))

if (n1 > n2) and (n1 > n3):
    nb = n1
elif (n2 > n1) and (n2 > n3):
    nb = n2
else:
    nb = n3
print("So lon nhat trong", n1, ",", n2, ",", n3, "la", nb)
