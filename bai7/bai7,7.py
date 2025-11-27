def count_lines(fname):
    """
    Hàm đếm số dòng trong tệp văn bản.
    """
    try:
        # Mở tệp ở chế độ đọc ('r')
        with open(fname, 'r') as f:
            # Đếm số lần lặp (số dòng) trong đối tượng tệp (iterator)
            line_count = sum(1 for line in f)
        return line_count
    except FileNotFoundError:
        return f"Lỗi: Không tìm thấy tệp '{fname}'"
    except Exception as e:
        return f"Lỗi không xác định: {e}"

# --- Ví dụ sử dụng ---
file_name = 'my_document.txt'

# GIẢ ĐỊNH: Bạn đã có tệp 'my_document.txt'
# Nếu chưa, bạn có thể tạo một tệp tạm thời cho mục đích thử nghiệm:
# with open(file_name, 'w') as f:
#     f.write("Đây là dòng 1.\n")
#     f.write("Đây là dòng 2.\n")
#     f.write("Đây là dòng 3.\n")


# Gọi hàm và in kết quả
result = count_lines(file_name)

if isinstance(result, int):
    print(f"✅ Tệp '{file_name}' có {result} dòng.")
else:
    print(f"❌ {result}")
