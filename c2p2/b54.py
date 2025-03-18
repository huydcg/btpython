def format_list(words):
    if not words:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

# Chương trình chính
def main():
    # Đọc các từ từ người dùng
    words = []
    while True:
        word = input("Nhập một từ (nhập dòng trống để kết thúc): ").strip()
        if word == "":
            break
        words.append(word)
    
    # Định dạng danh sách các từ
    formatted_string = format_list(words)
    
    # Hiển thị kết quả
    print("Danh sách các từ đã định dạng:")
    print(formatted_string)

# Gọi chương trình chính
if __name__ == "__main__":
    main()