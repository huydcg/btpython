def print_longer_string(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    if len1 > len2:
        print(str1)
    elif len2 > len1:
        print(str2)
    else:
        print(str1)
        print(str2)

# Đọc hai chuỗi từ người dùng
string1 = input("Nhập chuỗi thứ nhất: ")
string2 = input("Nhập chuỗi thứ hai: ")

# Gọi hàm để in chuỗi có độ dài lớn hơn
print_longer_string(string1, string2)