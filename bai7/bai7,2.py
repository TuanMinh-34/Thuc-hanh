# Sửa chữa và Tối ưu hóa chương trình đếm từ, ký tự, dòng
try:
    with open('D:/a.txt', 'r') as f:
        full_content = f.read() # Đọc toàn bộ nội dung file

    # 1. Đếm Ký tự (char):
    char_count = len(full_content)

    # 2. Đếm Dòng (line):
    # f.readlines() trả về danh sách các dòng, len() sẽ cho số dòng
    # Hoặc đơn giản là đếm ký tự xuống dòng '\n'
    line_count = full_content.count('\n') 

    # 3. Đếm Từ (word):
    # Lấy tất cả các từ bằng cách cắt chuỗi dựa trên khoảng trắng
    # và sau đó loại bỏ các chuỗi rỗng ('')
    words = full_content.split()
    word_count = len(words)

    # In ra kết quả cuối cùng
    print(f"✅ Kết quả Đếm File ✅")
    print(f"Số ký tự (char): {char_count}")
    print(f"Số từ (word): {word_count}")
    print(f"Số dòng (line): {line_count}")
    
except FileNotFoundError:
    print("❌ Lỗi: Không tìm thấy file 'D:/a.txt'. Hãy kiểm tra đường dẫn!")

# Lưu ý: Code này đếm SỐ DÒNG THẬT (có ký tự '\n'). 
# Nếu file kết thúc bằng một dòng không có ký tự xuống dòng, 
# cách đếm bằng readlines() hoặc count('\n') sẽ cần điều chỉnh thêm 1 tùy theo quy ước.
