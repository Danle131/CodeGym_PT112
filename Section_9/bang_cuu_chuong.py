# Sử dụng vòng lặp lồng nhau - Sinh bảng cửu chương
# sử dụng vòng lặp lồng nhau (for lồng for) để sinh bảng cửu chương từ 1 đến 9

for i in range (1,11):
    print(f"Bảng cửu chương {i}:")
    for j in range (1, 11):
        print(f'{i} x {j} = {i * j: 3}')
    print()
