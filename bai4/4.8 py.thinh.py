def tim_tu_dai_nhat_ngan_gon():
    # 1. Nhập và tách dãy từ
    day_tu = input("Nhập một dãy các từ: ")
    cac_tu = day_tu.split()
    
    if not cac_tu:
        print("\nKhông có từ nào được nhập.")
        return

    # 2. Tìm độ dài lớn nhất (Chỉ cần 1 dòng)
    # max() với key=len tìm ra từ dài nhất (và len() của từ đó)
    do_dai_lon_nhat = len(max(cac_tu, key=len))
    
    # 3. Lọc tất cả các từ có độ dài đó (List Comprehension)
    # Tạo danh sách ds_tu_dai_nhat bằng cách duyệt qua cac_tu 
    # và chỉ giữ lại những từ thỏa mãn len(tu) == do_dai_lon_nhat
    ds_tu_dai_nhat = [tu for tu in cac_tu if len(tu) == do_dai_lon_nhat]

    # 4. In kết quả
    print("\n--- KẾT QUẢ NGẮN GỌN ---")
    print(f"Độ dài lớn nhất: **{do_dai_lon_nhat}**")
    print("Các từ có độ dài lớn nhất là:")
    print(ds_tu_dai_nhat)
    
tim_tu_dai_nhat_ngan_gon()
