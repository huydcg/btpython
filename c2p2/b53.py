from itertools import combinations

def all_subsets(lst):
    # Tạo danh sách chứa mọi danh sách con
    subsets = []
    
    # Lặp qua tất cả các độ dài có thể của danh sách con
    for i in range(len(lst) + 1):
        # Sử dụng combinations để tạo các danh sách con có độ dài i
        for combo in combinations(lst, i):
            subsets.append(list(combo))
    
    return subsets

# Chương trình chính
def main():
    # Ví dụ danh sách đầu vào
    lst = [1, 2, 3]
    
    # Lấy tất cả các danh sách con
    result = all_subsets(lst)
    
    # Hiển thị kết quả
    print("Các danh sách con của", lst, "là:")
    for subset in result:
        print(subset)

# Gọi chương trình chính
if __name__ == "__main__":
    main()