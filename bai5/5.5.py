# Nhập danh sách
n = int(input("Nhập số lượng phần tử: "))
lst = [int(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]

# Tìm max, min
maximum = max(lst)
minimum = min(lst)

# Tìm vị trí (index)
vitri_max = lst.index(maximum)
vitri_min = lst.index(minimum)

# In kết quả
print("Phần tử lớn nhất:", maximum, "ở vị trí:", vitri_max)
print("Phần tử nhỏ nhất:", minimum, "ở vị trí:", vitri_min)
