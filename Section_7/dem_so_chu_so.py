# Nhập n nguyên dương, tính số chữ số của n
n = input("Nhập n: ")
if n.isdigit():
    x = int(n)
    i = 0
    while(x > 0):
        x//=10
        i+=1
    print("Số chữ số của n: ",i)
else:
    print("?!")
