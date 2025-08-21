# Sử dụng vòng lặp for

# Lặp qua danh sách
test_list = ["Tôi", "test", "lặp", "Python"]
for x in test_list:
    print(x, end = "_")
print()
# Lặp qua chuỗi
for x in "Hello World!":
    print(x, end = "")
print()
# Sử dụng range() để lặp số
for i in range (1, 9, 3):
    print(i, end = " ")
print()
# Lặp qua danh sách với chỉ mục (enumerate)
for thu_tu, element in enumerate(test_list):
    print(f'Phần tử thứ {thu_tu}: {element}')
    
