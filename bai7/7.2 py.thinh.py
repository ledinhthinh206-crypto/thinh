

FILE_PATH = "a.txt" 

try:
    with open(FILE_PATH, 'w') as f_setup:
        f_setup.write("Day la dong thu nhat.\n")
        f_setup.write("Dong thu hai va cuoi cung.\n")
    print(f"✅ Created sample file: '{FILE_PATH}'")
except Exception as e:
    print(f"❌ Cannot create sample file: {e}")

    exit()

try:

    k = open(FILE_PATH, 'r') 

    char, wc, lc = 0, 0, 0 

    for line in k:
        lc = lc + 1 
        
        for char_index in range(0, len(line)):
            char = char + 1 
           
            if (line[char_index] == ' '):
                wc = wc + 1
    k.close() 

    print("---------------------------------")
    print("The no.of chars is %d\n The no.of words is %d\n The no.of lines is %d"%(char, wc, lc))

except FileNotFoundError:
    print(f"❌ Lỗi: File not found at {FILE_PATH}. Vui lòng kiểm tra lại quyền truy cập file.")
except Exception as e:
    print(f"❌ Đã xảy ra lỗi khác: {e}")
