# Nhập chuỗi từ bàn phím
ds = input('Nhap day cac tu: ').split()

# Tìm độ dài lớn nhất trong danh sách
max_len = max(len(tu) for tu in ds)

# In ra tất cả các từ có độ dài bằng max_len
print('Cac tu dai nhat la:')
for tu in ds:
    if len(tu) == max_len:
        print(tu)
