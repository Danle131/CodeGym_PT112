def sum_n(n):
    return n*(n+1)/2
so_n = input("Nhập số n: ")
if so_n.isdigit():
    x = int(so_n)
    if x >= 1:
        print(f'Tổng các giá trị từ 1 đến {x} là: {sum_n(x):.0f}')
    else:
        print("?!")
else:
    print("?!")
