n=int(input("Nhap so nguyen lon hon 0: "))
sum=0.0
for i in range(1,n+1):
    sum += float(float(i) / (i + 1))
    if (i < n):
        print(i, "/", (i + 1), "+")
    else:
        print(i, "/", (i + 1),"=", sum)