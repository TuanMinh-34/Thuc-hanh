from mymodule import sort_list, find_max, find_min

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử của danh sách: "))

lst = []
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

print("\nDanh sách ban đầu:", lst)

# Gọi module để xử lý
sorted_list = sort_list(lst)
largest = find_max(lst)
smallest = find_min(lst)

print("Danh sách sau khi sắp xếp:", sorted_list)
print("Phần tử lớn nhất:", largest)
print("Phần tử nhỏ nhất:", smallest)

# Tìm vị trí trong danh sách ban đầu
max_index = lst.index(largest)
min_index = lst.index(smallest)

print("Vị trí phần tử lớn nhất:", max_index)
print("Vị trí phần tử nhỏ nhất:", min_index)
