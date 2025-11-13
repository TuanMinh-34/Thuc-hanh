import numpy as np

# Định nghĩa cấu trúc dữ liệu (kiểu dữ liệu cho từng cột)
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu sinh viên: (tên, lớp, chiều cao)
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

# Sắp xếp mảng theo chiều cao (cột 'height')
print("\nSort by height:")
print(np.sort(students, order='height'))
