# Tiếp tục trong file search_algorithms.py

def binary_search(list_data, value):
    """
    Thực hiện tìm kiếm nhị phân trên danh sách đã sắp xếp list_data cho phần tử value.
    Trả về True nếu tìm thấy, ngược lại là False.
    """
    # Yêu cầu tiên quyết cho tìm kiếm nhị phân: danh sách phải được sắp xếp.
    # Hàm này giả định rằng list_data đã được sắp xếp trước khi gọi.

    low = 0
    high = len(list_data) - 1

    while low <= high:
        mid = (low + high) // 2  # Sử dụng phép chia lấy phần nguyên
        if list_data[mid] == value:
            return True
        elif list_data[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Ví dụ gợi ý:
# print(binary_search([1,2,3,5,8], 6)) # -> False
# print(binary_search([1,2,3,5,8], 5)) # -> True
