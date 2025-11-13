import datetime as dt

# Định dạng thời gian đầu vào
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển chuỗi thời gian sang đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In ra các thành phần của thời gian t1
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))

# Lấy thời gian hiện tại của hệ thống
t2 = dt.datetime.now()

# Tính hiệu giữa hai thời điểm (kết quả là một đối tượng timedelta)
diff = t2 - t1

# In ra số ngày chênh lệch
print('How many days difference? ' + str(diff.days))
