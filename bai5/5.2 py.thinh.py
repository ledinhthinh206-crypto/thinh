import datetime as dt

# SỬA LỖI Ở ĐÂY: Thêm 'T' vào chuỗi định dạng
format = '%Y-%m-%dT%H:%M:%S'
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In các thành phần của đối tượng datetime t1
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))

# Định nghĩa thời gian hiện tại
t2 = dt.datetime.now()
diff = t2 - t1

# In sự khác biệt về số ngày
print('How many days difference? ' + str(diff.days))
