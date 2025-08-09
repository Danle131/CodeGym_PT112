# Viết chương trình nhập vào điểm 3 môn học và:
# Tính điểm trung bình
# Phân loại học lực: Giỏi (>=8), Khá (>=6.5), Trung bình (>=5), Yếu (<5)

a = float(input("Nhập điểm môn 1: "))
b = float(input("Nhập điểm môn 2: "))
c = float(input("Nhập điểm môn 3: "))
xep_loai = ["Giỏi", "Khá", "Trung bình", "Yếu"]

mean = float((a+b+c)/3)

if mean >= 8:
    result = xep_loai[0]
elif 8 > mean >= 6.5:
    result = xep_loai[1]
elif 6.5 > mean >= 5:
    result = xep_loai[2]
else:
    result = xep_loai[3]

print(f'Điểm trung bình: {mean:.2f}\nXếp loại: {result}')
