a = input("Nhập chuỗi cần kiểm tra: ").lower()
b = input("Nhập từ cần tìm: ").lower()
l = a.count(b)
if (l == 0):
    print("Không tồn tại từ cần tìm trong chuỗi đầu vào")
else:
    print(l)
