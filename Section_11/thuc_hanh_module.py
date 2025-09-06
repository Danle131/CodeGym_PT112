# # BÀI TẬP LUYỆN TẬP MODULE PYTHON
import random
import datetime
import math

# ## 📐 PHẦN 1: MODULE MATH

# ### Bài 1: Máy tính cơ bản
# Viết chương trình nhập 2 số a, b và thực hiện:
# - Tính căn bậc 2 của a
# - Tính a^b (lũy thừa)
# - Tính log cơ số 10 của a
# - Làm tròn b lên và xuống

def bai1(a, b):
    print(f'Căn bậc 2 của a = {math.sqrt(a)}')
    print(f'Giá trị của a^b = {math.pow(a,b)}')
    print(f'Giá trị của log_10(a) = {math.log10(a)}')
    print(f'Giá trị của b làm tròn lên = {math.ceil(b)} \n Giá trị của b làm tròn xuống = {math.floor(b)}')

# ### Bài 2: Tính khoảng cách
# Nhập tọa độ 2 điểm A(x1,y1) và B(x2,y2), tính khoảng cách AB
# Công thức: √[(x2-x1)² + (y2-y1)²]

def bai2(x1,y1,x2,y2):
    print(f'Khoảng cách giữa 2 điểm A và B trong hệ tọa độ = {math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))}')

# ### Bài 3: Tính diện tích hình tròn
# Nhập bán kính r, tính:
# - Diện tích hình tròn (π × r²)
# - Chu vi hình tròn (2 × π × r)

def bai3(R):
    print(f'Diện tích hình tròn = {math.pow(R,2)*math.pi}')
    print(f'Chu vi hình tròn = {2*math.pi*R}')

# ## 🎲 PHẦN 2: MODULE RANDOM

# ### Bài 4: Game đoán số
# - Máy tính chọn ngẫu nhiên một số từ 1-100
# - Người chơi đoán, máy tính báo "lớn hơn" hay "nhỏ hơn"
# - Đếm số lần đoán

def bai4():
    a = random.uniform(1,100)
    guess = input("Đoán số ngẫu nhiên")
    if a > guess:
        print(f'Số bạn đoán nhỏ hơn số được generate ({a})')
    elif a == guess:
        print(f'Bạn đoán đúng số được generate (xác suất đoán trúng là bằng 0, how?)')
    else:
        print(f'Số bạn đoán to hơn số được generate ({a})')

# ### Bài 5: Tung xúc xắc
# - Mô phỏng tung 2 xúc xắc 1000 lần
# - Đếm xem có bao nhiều lần tổng = 7
# - Tính tỷ lệ phần trăm
def bai5():
    xuat_hien = 0
    for i in range(1000):
        xuc_xac_1 = random.randint(1, 6)
        xuc_xac_2 = random.randint(1, 6)
        tong = xuc_xac_1 + xuc_xac_2
        if tong == 7:
            xuat_hien+=1
    print(f'Tỉ lệ xuất hiện (omega = 1000) = {xuat_hien/1000}')

# ### Bài 6: Random password
# Tạo mật khẩu ngẫu nhiên có:
# - 8 ký tự
# - Gồm chữ hoa, chữ thường, số, ký tự đặc biệt
import string
def bai6():
    a = int(input("Nhập vào độ dài mong muốn của mật khẩu: "))
    all_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    character_list = list(all_characters)
    password = random.choices(character_list, a)
    print(f'Generated Password: ', end = "")
    for x in password:
        print(x, end="")
    print()
    
# ---

# ## 📅 PHẦN 3: MODULE DATETIME

# ### Bài 7: Tính tuổi chính xác
# - Nhập ngày sinh (dd/mm/yyyy)
# - Tính tuổi chính xác (năm, tháng, ngày)
def bai7():
    birthday = input("Nhập ngày sinh (dd/mm/yyyy): ")
    ngaysinh = datetime.strptime(birthday, "%d/%m/%Y")
    hientai = datetime.now()
    tuoi = hientai.year() - ngaysinh.year()
    if(ngaysinh.month(), ngaysinh.day < hientai.month(), hientai.day()): 
        tuoi-=1
    print("Tuổi hiện tại = ", tuoi)
    print()

# ### Bài 8: Đếm ngược
# - Nhập một ngày trong tương lai
# - Đếm còn bao nhiều ngày nữa đến ngày đó
def bai8():
    hientai = datetime.today()
    try:
        tuonglai = input("Nhập một ngày trong tương lai (dd/mm/YYYY): ")
        tlai = datetime.strptime(tuonglai, "d%/%m/%Y")
        print(f'Số ngày còn lại tới ngày đó {(tlai - hientai).days}')
    except ValueError:
        print("Ưhat the f bro?\n")
