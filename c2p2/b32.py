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

def caesar_decipher(text, shift):
    # Giải mã bằng cách dịch chuyển ngược lại
    return caesar_cipher(text, -shift)

# Đọc tin nhắn từ người dùng
message = input("Nhập tin nhắn: ")

# Đọc số ký tự dịch chuyển từ người dùng
shift = int(input("Nhập số ký tự dịch chuyển: "))

# Chọn chức năng mã hóa hoặc giải mã
choice = input("Bạn muốn mã hóa hay giải mã tin nhắn? (m/g): ").strip().lower()

if choice == "m":
    # Mã hóa tin nhắn
    encrypted_message = caesar_cipher(message, shift)
    print("Tin nhắn đã được mã hóa:", encrypted_message)
elif choice == "g":
    # Giải mã tin nhắn
    decrypted_message = caesar_decipher(message, shift)
    print("Tin nhắn đã được giải mã:", decrypted_message)
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn 'mã hóa' hoặc 'giải mã'.")