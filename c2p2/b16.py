n=int(input("Nhập vào một số:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)

print(" ".join(map(str, d.keys())))

print(" ".join(map(str, d.values())))

for key in d.keys():
    print(key,end=" ")

print()

for value in d.values():
    print(value,end=" ")