def cat_list_bo_dau_cuoi():
    # 1. Nhập list từ bàn phím
    ds = input('Nhập các phần tử (cách nhau bởi dấu cách, ví dụ: 1 2 3 4 5): ').split()
    
    # 2. Kiểm tra điều kiện cần thiết: List phải có ít nhất 3 phần tử (để có thể bỏ đầu và cuối)
    if len(ds) < 3:
        print("\nCảnh báo: List quá ngắn. Cần ít nhất 3 phần tử để bỏ phần tử đầu và cuối.")
        print(f"List gốc: {ds}")
        return

    # 3. Cắt list: Lấy từ index 1 (bỏ phần tử đầu) đến index -1 (bỏ phần tử cuối)
    x = ds[1:-1] 

    # 4. In kết quả theo yêu cầu đề bài
    print("\n--- KẾT QUẢ CẮT LIST ---")
    print(f"List gốc (ds): {ds}")
    print(f"List đã cắt (x): **{x}**")
    
    print("\nIn từng phần tử của list đã cắt:")
    # In từng phần tử, mỗi phần tử một dòng
    for c in x:
        print(c)

# Chạy hàm
cat_list_bo_dau_cuoi()
