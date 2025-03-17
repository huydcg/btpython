numlist = list()
while (True):
    inp = input("Enter a number: ")
    if inp == "s": break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Giá trị trung bình:", average)
print(numlist)