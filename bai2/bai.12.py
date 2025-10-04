import re

mat_khau_hop_le = []  

nhap_vao = input("Nhập danh sách mật khẩu (cách nhau bởi dấu phẩy): ")
danh_sach_mat_khau = [x for x in nhap_vao.split(',')]

for mat_khau in danh_sach_mat_khau:
    if len(mat_khau) < 6 or len(mat_khau) > 12:
        continue

    if not re.search("[a-z]", mat_khau): 
        continue
    elif not re.search("[0-9]", mat_khau): 
        continue
    elif not re.search("[A-Z]", mat_khau): 
        continue
    elif not re.search("[$#@]", mat_khau): 
        continue
    elif re.search("\s", mat_khau):
        continue
    else:
        mat_khau_hop_le.append(mat_khau) 

print("Mật khẩu hợp lệ là:", ",".join(mat_khau_hop_le))
