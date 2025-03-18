# Tuple cho trước
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Tạo tuple chứa các phần tử là số chẵn
even_tuple = tuple(num for num in t if num % 2 == 0)

# In ra tuple chứa các số chẵn
print("Tuple chứa các số chẵn:", even_tuple)