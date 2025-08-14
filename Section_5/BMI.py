# Viết chương trình tính chỉ số BMI
# BMI < 18.5: Thiếu cân
# 18.5 ≤ BMI < 24.9: Bình thường
# 25 ≤ BMI < 29.9: Thừa cân
# BMI ≥ 30: Béo phì

mass = float(input("Cân nặng (kg): "))
height = float(input("Chiều cao (m): "))
BMI = mass / (height ** 2)

print(f'Chỉ số BMI: {BMI}')

if BMI < 18.5:
    print("Bạn đang thiếu cân")
elif 18.5 <= BMI < 24.9:
    print("Bạn bình thường")
elif 25 <= BMI < 29.9:
    print("Bạn thừa cân")
else:
    print("Bạn béo phì")
