st = input("Nhap chuoi cua ban: ")
st_search = input("Chuoi can tim: ")
if st_search in st:
    print("Chuoi da tim thay o vi tri: " + str(st.find(st_search)))
else:
    print("Khong tim thay")