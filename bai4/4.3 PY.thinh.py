S = input('Nhập chuỗi: ')

print('--- Kết quả in HOA ---')
for ch in S:
    # 1. Chuyển ký tự 'ch' sang dạng chữ IN HOA bằng .upper()
    ch_hoa = ch.upper()
    
    # 2. In ký tự đã chuyển
    print(ch_hoa)
