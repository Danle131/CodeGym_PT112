# Viết chương trình in ra các số chẵn đầu tiên

n = input("Nhập số số chẵn cần in: ")
if n.isdigit():
    x = int(n)
    if (x < 0):
        print("?!")
    elif x == 0:
        print("Không số nào cả")
    else:
        for i in range(2, (x - 1)*2 + 3, 2):
            print(i, end = " ")
else:
    print("?!")

