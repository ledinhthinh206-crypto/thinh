# Định nghĩa hàm get_sum(*num)
# Dấu *num cho phép hàm nhận VÀ ĐÓNG GÓI một số lượng đối số bất kỳ
# thành một tuple có tên là 'num'.
def get_sum(*num):
    tmp = 0 
    
    # Duyệt qua từng phần tử (i) trong tuple 'num'
    for i in num:
        # Cộng giá trị của i vào biến tmp
        tmp += i
        
    # Trả về tổng cuối cùng
    return tmp

# Gọi hàm get_sum() với 5 đối số và gán kết quả trả về vào biến 'result'
# num sẽ là: (1, 2, 3, 4, 5)
result = get_sum(1, 2, 3, 4, 5)

# In kết quả
print(result)

# Thử một ví dụ khác với số lượng tham số khác:
result_new = get_sum(10, 20, 30)
print(result_new)
