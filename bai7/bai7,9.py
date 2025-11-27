def copy_file_line_by_line(source_file, destination_file):
    """
    Sao chép nội dung từ tệp nguồn sang tệp đích bằng cách đọc từng dòng.
    """
    try:
        # Mở tệp nguồn để đọc ('r')
        with open(source_file, 'r', encoding='utf-8') as f_source:
            # Mở tệp đích để ghi ('w')
            with open(destination_file, 'w', encoding='utf-8') as f_dest:
                # Lặp qua từng dòng của tệp nguồn
                for line in f_source:
                    f_dest.write(line) # Ghi dòng đó sang tệp đích
        
        print(f"✅ Đã sao chép nội dung từ '{source_file}' sang '{destination_file}' thành công.")
    
    except FileNotFoundError:
        print(f"❌ Lỗi: Không tìm thấy tệp nguồn '{source_file}'.")
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi: {e}")

# --- Ví dụ sử dụng ---
source = 'source.txt'
destination = 'destination.txt'

# Lưu ý: Cần đảm bảo 'source.txt' đã tồn tại trước khi chạy.
# Ví dụ tạo tệp nguồn:
# with open(source, 'w', encoding='utf-8') as f:
#     f.write("Đây là nội dung gốc.\n")
#     f.write("Dòng thứ hai cần được sao chép.")

copy_file_line_by_line(source, destination)
