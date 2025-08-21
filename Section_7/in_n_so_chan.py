# Viết chương trình cho phép người dùng nhập vào một số nguyên dương N. Sử dụng vòng lặp while để in ra tất cả các số chẵn từ 1 đến N.

n = input("Nhập n: ")
if n.isdigit():
    x = int(n)
    if x == 1:
        print("Không có số nào")
    else:
        i = 2
        while(i <= x):
            print(i, end = " ")
            i+=2
else:
    print("?!")
