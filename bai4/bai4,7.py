chuoi = input('Nhap chuoi: ')
ket_qua = ''

for ch in chuoi:
    if not ch.isdigit():   # nếu ký tự KHÔNG phải là chữ số
        ket_qua += ch       # thì thêm vào chuỗi kết quả

print('Chuoi sau khi loai bo chu so:', ket_qua)
