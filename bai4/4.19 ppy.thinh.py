LIMIT = 1000000

# Khởi tạo mảng boolean. is_prime[i] = True nếu i là số nguyên tố
is_prime = [True] * LIMIT 
is_prime[0] = is_prime[1] = False # 0 và 1 không phải là số nguyên tố

# Tiến hành Sàng Eratosthenes
p = 2
while (p * p) < LIMIT: 
    if is_prime[p]:
        # Đánh dấu tất cả các bội số của p là False
        # Bắt đầu từ p*p để tối ưu
        for i in range(p * p, LIMIT, p):
            is_prime[i] = False
    p += 1

# Tạo list các số nguyên tố (chỉ duyệt qua các vị trí True)
list_nguyen_to = [p for p, is_p in enumerate(is_prime) if is_p]

# Chuyển list sang tuple P theo yêu cầu
P = tuple(list_nguyen_to)

# In kết quả (có thể bỏ qua nếu chỉ cần nộp code)
print(f"Tổng số lượng số nguyên tố < {LIMIT}: {len(P)}")
print(f"Tuple P bắt đầu bằng: {P[:10]}...")
