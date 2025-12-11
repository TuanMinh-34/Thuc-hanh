import numpy as np

# Dữ liệu đầu vào
students = np.array([('James', 5, 48.5 ), ('Nail', 6, 52.5 ), ('Paul', 5, 42.1 ), ('Pit', 5, 40.11)],
                  dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

# Sắp xếp theo lớp, sau đó là chiều cao nếu lớp bằng nhau
sorted_students = np.sort(students, order=['class', 'height'])

print("Kết quả sắp xếp:")
print(sorted_students)
