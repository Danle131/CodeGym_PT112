# Bài 1: Học phí sinh viên
# Viết chương trình tính học phí dựa trên loại sinh viên dựa trên số tín chỉ (input từ bàn phím).
# Nếu là sinh viên chính quy: Học phí là 100 USD/tín chỉ. Nếu đăng ký >15 tín chỉ, giảm 10 $ trên mỗi tín chỉ đã đăng ký.
# Nếu không phải chính quy: Học phí là 150 USD/tín chỉ, không giảm giá.

so_tin = int(input("Nhập số tín chỉ: "))
flag_cq = int(input("Bạn có là sinh viên chính quy không? (1: Có | 0: Không): "))
hoc_phi = 0
if flag_cq == 1:
    if so_tin > 15:
        hoc_phi = 100*15 + (so_tin - 15)*90
    else:
        hoc_phi = 100*so_tin
else:
    hoc_phi = 150*so_tin
print(f'Học phí kì này: {hoc_phi}')
