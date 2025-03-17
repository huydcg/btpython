total = 0
count = 0
while (True):
    inp = input("Nhập một số: ")
    if inp == "s":
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print("Giá trị trung bình:", average)