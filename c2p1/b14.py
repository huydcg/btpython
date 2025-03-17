from math import *

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

s = a + b
d = a - b
p = a * b
q = a / b
du = a % b
log_a = log10(a)
amb = a ** b

print("a + b : " + str(s))
print("a - b : " + str(d))
print("a * b : " + str(p))
print("a / b : " + str(q))
print("a chia b dư : " + str(du))
print("log10(a): " + str(round(log_a,4)))
print("a mũ b : "+ str(amb))