# Viết chương trình vẽ tam giác
height = input("Nhập chiều cao tam giác: ")

while height.isdigit():
    x = int(height)

    # Vẽ tam giác ver1
    for i in range (1, x + 1):
        for j in range (i):
            print("#", end = "")
        print()  

    print()

    # Vẽ tam giác ver2
    for i in range(x, -1, -1):
        for j in range (i, 0, -1):
            print(j, end = " ")
        print()      

    print()

    # Vẽ tam giác ver3
    step = 1
    for i in range(x, 2*x):
        j = 1
        while (j <= x - step):
            print(" ", end = "")
            j += 1
        for l in range(j, i + 1):
                print("#", end = "")
        print()
        step+=1
        j = 1
    break


