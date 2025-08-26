# Dãy Fibonacci là một dãy số trong đó mỗi số là tổng của hai số trước đó. Công thức tổng quát:
# F(n) = F(n-1) + F(n-2)
# Với điều kiện:
# F(0) = 0
# F(1) = 1
# Chương trình yêu cầu nhập một số nguyên n và in ra n số Fibonacci đầu tiên.

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    t = 0
    for i in range(n + 1):
        if i < 2:
            continue
        t = a + b
        a = b
        b = t
    return b
n_str = input("Nhập số n: ")
if n_str.isdigit():
    n = int(n_str)
    if n > 0:
        for i in range(n + 1):
            print(f'Số fibonacci thứ {i} = {fibo(i)}')
