# Nhập tên từ bàn phím
hoten = input('Nhap ho va ten: ')

# Tách thành danh sách gồm 2 phần: họ và tên riêng
ds = hoten.split()

# Gán biến họ và tên riêng
ho = ds[0]
ten = ds[1]

# In ra kết quả
print('Ho la:', ho)
print('Ten rieng la:', ten)
