# In dãy số từ 1 đến 5 bằng while
# Lặp cho đến khi người dùng nhập đúng dữ liệu
# Sử dụng while với danh sách
# Dừng vòng lặp bằng break

i = 0
while i <= 5:
    print(i)
    i += 1
while 1:
    inp = int(input("Nhập một số nguyên từ 100 đến 500: "))
    if(inp in range(100,500)):
        print(f'Nice, bạn làm theo luật lệ, điều không ai ép')
        break
    else:
        print("?!")

list = [] 
for i in range (1, inp + 1, 50):
    list.append(i)

print(f"Tôi sẽ in ra một số số nguyên thuộc [1;{inp + 1}), step = 50")
for x in list:
    print(x)

