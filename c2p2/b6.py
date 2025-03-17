st = input("Nhap vao mot cau: ")
Sum_upper_Char = 0
Sum_lower_Char = 0
for c in st:
    if c.isupper():
        Sum_upper_Char +=1
    elif c.islower():
        Sum_lower_Char +=1
    else:
            pass
print("Tong ky tu hoa:", Sum_upper_Char)
print("Tong ky tu thuong:", Sum_lower_Char)