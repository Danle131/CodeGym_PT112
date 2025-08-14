# Người dùng nhập điểm trung bình của sinh viên.
# Đảm bảo rằng giá trị nhập vào là số hợp lệ.
# Điểm ≥ 8.5: Giỏi
# 7.0 ≤ Điểm < 8.5: Khá
# 5.0 ≤ Điểm < 7.0: Trung bình
# Điểm < 5.0: Yếu

diem_str = input("Nhập điểm trung bình của sinh viên (0 - 10): ")

if diem_str.isdigit():
    diem = float(diem_str)
    if 0 <= diem <= 10:
        if diem < 5:
            print("Yếu")
        elif diem < 7:
            print("Trung bình")
        elif diem < 8.5:
            print("Khá")
        else:
            print("Giỏi")
    else:
        print("Điểm nằm ngoài khoảng 0–10")
else:
    print("Giá trị nhập không hợp lệ (phải là số)")
