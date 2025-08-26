# [Thực hành 4]: Yêu cầu:
# Chương trình cho phép nhập điểm của 5 sinh viên.
# Quy tắc:
# Nếu điểm nhập âm → continue (bỏ qua, không tính).
# Nếu điểm nhập = 0 → dùng pass (coi như bỏ qua không xử lý, nhưng vẫn tính vào số lượng SV).
# Nếu điểm nhập = 100 → coi là điểm đặc biệt → break và dừng nhập sớm.
# Sau khi nhập xong: tính trung bình các điểm hợp lệ (>0).

so_luong_fake = input("Nhập số lượng sinh viên cần tính: ")
if so_luong_fake.isdigit():
    size_temp = int(so_luong_fake)
    if size_temp > 0:
        values = [input(f"Nhập điểm số của sinh viên {i + 1}: ") for i in range(size_temp)]
    else:
        print("?!")
else:
    print("?!")

size = 0
dtb = 0
for diem_str in values:
    if diem_str.isdigit():
        diem = int(diem_str)
        if diem == 100:
            size +=1
            dtb += diem
            break
        elif diem < 0:
            continue
        elif diem == 0:
            size +=1
        elif diem != 100:
            size +=1
            dtb += diem
if size == 0:
    print("Toàn điểm âm?")
else:
    print(f'Trung bình các điểm hợp lệ = {dtb / size:.2f}')
