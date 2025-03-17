num = int(input("Nhập một số: "))
bac = int(input("Bậc: "))
sum = 0 # tổng
temp = num # 1 số = num
while temp > 0:
    digit = temp % 10 # tách từng số
    sum += digit ** bac # số tách lũy thừa lên
    temp //= 10 # chia lấy nguyên số temp để tiếp vòng lặp while
if num == sum:
    print(num, "là số Amstrong, bậc: " + str(bac))
else:
    print(num, "không phải là số Amstrong")