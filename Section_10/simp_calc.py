# Bài tập này yêu cầu xây dựng một chương trình máy tính đơn giản thực hiện các phép toán: cộng, trừ, nhân, chia. 
# Người dùng sẽ nhập vào hai số và chọn phép toán muốn thực hiện.

def simp_calc(a, b, *args):
    for x in args:
        if x == "+":
            print(f'Tổng a + b = {a + b}')
        elif x == "-":
            print(f'Hiệu a - b = {a - b}')
        elif x == "*":
            print(f'Tích a * b = {a * b}')
        elif x == "/":
            print(f'Thương a / b = {a / b}')
        else:
            print("Máy này cùi lắm, cộng trừ nhân chia thôi :(((")

a_str = input("Nhập số a: ")
b_str = input("Nhập số b: ")
n = int(input("Nhập số các phép toán cần tính: "))
calc = [input(f"Nhập các phép toán cần tính thứ {i + 1} (+, -, *, /): ") for i in range(n)]
if a_str.isdigit() and b_str.isdigit():
    a = int(a_str)
    b = int(b_str)
    simp_calc(a,b, *calc)
