# Viết chương trình nhập vào điểm 3 môn học và:
# Tính điểm trung bình
# Phân loại học lực: Giỏi (>=8), Khá (>=6.5), Trung bình (>=5), Yếu (<5)
# Không dùng if else

a = float(input("Nhập điểm môn 1: "))
b = float(input("Nhập điểm môn 2: "))
c = float(input("Nhập điểm môn 3: "))

mean = float((a+b+c)/3)

xep_loai = ["Yếu", "Trung bình", "Khá", "Giỏi"]
moc = [5, 6.5, 8]
thu_tu = sum(mean >= x for x in moc)

print(f'Điểm trung bình: {mean:.2f}\nXếp loại: {xep_loai[thu_tu]}')
