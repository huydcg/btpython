
cost = float(input("Nhập chi phí bữa ăn: "))

tip = cost * 0.18

tax = cost * 0.05

cost_real = cost - tip - tax

print("Tổng tiền: " + str(cost))
print("Tiền boa: " + str(round(tip, 2)))
print("Tiền thuế: " + str(round(tax, 2)))
print("Tiền bữa ăn: "+ str(round(cost_real, 2)))
