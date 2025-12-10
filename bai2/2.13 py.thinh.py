import math

def giai_phuong_trinh_bac_hai():
    print("--- Chương trình Giải Phương trình bậc 2: ax^2 + bx + c = 0 ---")
    
    # 1. Nhập hệ số từ bàn phím
    try:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
    except ValueError:
        print("Lỗi: Hệ số phải là giá trị số.")
        return

    # 2. Xử lý trường hợp a = 0 (Phương trình bậc nhất)
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            # Phương trình bậc nhất: bx + c = 0
            x = -c / b
            print(f"Phương trình là bậc nhất: {b}x + {c} = 0")
            print(f"Phương trình có 1 nghiệm duy nhất: x = {x:.4f}")
        return

    # 3. Tính Delta (Biệt thức)
    # Công thức: Delta = b^2 - 4ac
    delta = b**2 - 4*a*c
    print(f"\nGiá trị Delta (Δ) = {delta:.4f}")

    # 4. Phân loại và tìm nghiệm
    
    if delta > 0:
        # Trường hợp Delta > 0: Hai nghiệm thực phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm thực phân biệt:")
        print(f"x1 = {x1:.4f}")
        print(f"x2 = {x2:.4f}")
        
    elif delta == 0:
        # Trường hợp Delta = 0: Một nghiệm kép
        x = -b / (2*a)
        print("Phương trình có nghiệm kép:")
        print(f"x = {x:.4f}")
        
    else: # delta < 0
        # Trường hợp Delta < 0: Hai nghiệm phức
        # Sử dụng giá trị tuyệt đối của Delta cho phần ảo
        phan_thuc = -b / (2*a)
        phan_ao = math.sqrt(abs(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phức:")
        print(f"x1 = {phan_thuc:.4f} + {phan_ao:.4f}i")
        print(f"x2 = {phan_thuc:.4f} - {phan_ao:.4f}i")

# Gọi hàm để chạy chương trình
giai_phuong_trinh_bac_hai()
