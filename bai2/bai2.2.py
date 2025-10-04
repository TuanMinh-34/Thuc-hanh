import math 

x1 = float(input("Nhập hoành độ điểm thứ nhất (x1): "))
y1 = float(input("Nhập tung độ điểm thứ nhất (y1): "))

x2 = float(input("Nhập hoành độ điểm thứ hai (x2): "))
y2 = float(input("Nhập tung độ điểm thứ hai (y2): "))

khoang_cach = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Khoảng cách giữa hai điểm là:", khoang_cach)
