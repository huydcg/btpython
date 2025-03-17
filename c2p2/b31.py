def caesar_cipher(text, shift):
    result = ""

    for char in text:
        # Kiểm tra nếu ký tự là chữ cái
        if char.isalpha():
            # Xác định mã ASCII của ký tự đầu tiên (A hoặc a)
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Tính toán vị trí mới của ký tự sau khi dịch chuyển
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            # Giữ nguyên các ký tự không phải chữ cái
            result += char

    return result

# Đọc tin nhắn từ người dùng
message = input("Nhập tin nhắn cần mã hóa: ")

# Dịch chuyển 3 vị trí
shift = 3

# Mã hóa tin nhắn
encrypted_message = caesar_cipher(message, shift)

# Hiển thị tin nhắn đã được mã hóa
print("Tin nhắn đã được mã hóa:", encrypted_message)