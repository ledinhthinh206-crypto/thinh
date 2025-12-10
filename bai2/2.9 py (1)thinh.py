from collections import Counter

str_input = input("Enter a String:")
count_dict = Counter(str_input)
print(count_dict)
# Lưu ý: Kết quả in ra sẽ là một đối tượng Counter, nhưng nó hoạt động như một từ điển.
