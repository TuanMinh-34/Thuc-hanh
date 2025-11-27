def write_list_to_file_fast(file_name, my_list):
    """
    Viết nội dung danh sách vào tệp bằng writelines, mỗi phần tử là một dòng.
    Yêu cầu phải thêm '\n' vào cuối mỗi phần tử.
    """
    # Tạo một danh sách mới với ký tự xuống dòng ở cuối mỗi phần tử
    lines_to_write = [item + '\n' for item in my_list]
    
    try:
        # Mở tệp ở chế độ ghi ('w'). Nếu tệp không tồn tại, nó sẽ được tạo. 
        # Nếu tệp đã tồn tại, nội dung cũ sẽ bị ghi đè.
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(lines_to_write)
        print(f"✅ Đã ghi {len(my_list)} mục vào tệp '{file_name}' thành công.")
        
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi: {e}")

# --- Ví dụ sử dụng ---
data_list = ["Táo", "Cam", "Chuối", "Nho", "Xoài"]
file_output = 'danh_sach_trai_cay.txt'

write_list_to_file_fast(file_output, data_list)
