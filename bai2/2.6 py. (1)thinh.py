# Bước 1: Khởi tạo danh sách
ket_qua = []

# Bước 2: Lặp qua phạm vi 2000 đến 3200
for so in range(2000, 3201):
    
    # Bước 3: Kiểm tra điều kiện (chia hết cho 7 VÀ không chia hết cho 5)
    if (so % 7 == 0) and (so % 5 != 0):
        
        # Bước 4: Thêm số vào danh sách (chuyển sang chuỗi)
        ket_qua.append(str(so))

# Bước 5: In kết quả, nối bằng dấu phẩy
print(','.join(ket_qua))
