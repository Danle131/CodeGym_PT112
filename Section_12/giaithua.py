try:
    n = int(input("Nhập số n: "))
except ValueError:
    print("gif v bro?!")
def giaithua(a):
    if a <= 1:
        return 1
    else:
        return a * giaithua(a - 1)

print(f'Giai thừa của n = {giaithua(n)}')
