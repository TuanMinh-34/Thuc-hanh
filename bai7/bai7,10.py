import re

def find_longest_words(file_name):
    """
    Tìm tất cả các từ dài nhất trong tệp văn bản.
    """
    max_length = 0
    longest_words = set()

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()

        # 1. Tách văn bản thành các từ
        # Tách dựa trên khoảng trắng và loại bỏ các ký tự không phải chữ cái/số
        # re.findall(r'\b\w+\b', text) là cách hiệu quả để tìm các "từ"
        words = re.findall(r'\b\w+\b', text.lower())

        if not words:
            return "Tệp không chứa bất kỳ từ nào."

        # 2. Tìm độ dài tối đa
        for word in words:
            if len(word) > max_length:
                max_length = len(word)

        # 3. Lọc và lưu trữ tất cả các từ có độ dài tối đa
        for word in words:
            if len(word) == max_length:
                longest_words.add(word) # Dùng set để tránh các từ trùng lặp

        # 4. Trả về kết quả
        result = {
            "longest_words": list(longest_words),
            "max_length": max_length
        }
        return result

    except FileNotFoundError:
        return f"Lỗi: Không tìm thấy tệp '{file_name}'."
    except Exception as e:
        return f"Lỗi không xác định: {e}"

# --- Ví dụ sử dụng ---
file_to_analyze = 'van_ban_mau.txt'

# GIẢ SỬ 'van_ban_mau.txt' có nội dung: 
# "Chương trình Python là một ngôn ngữ tuyệt vời, chương trình này được viết ra để tìm từ dài nhất."

# Tạo tệp mẫu (nếu chưa có)
try:
    with open(file_to_analyze, 'w', encoding='utf-8') as f:
        f.write("Chương trình Python là một ngôn ngữ tuyệt vời, chương trình này được viết ra để tìm từ dài nhất.")
except:
    pass


result = find_longest_words(file_to_analyze)

if isinstance(result, dict):
    print(f"✅ Độ dài tối đa của từ tìm được là: **{result['max_length']}** ký tự.")
    print("Các từ dài nhất là:")
    for word in result['longest_words']:
        print(f"- {word}")
else:
    print(f"❌ {result}")
