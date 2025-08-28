# Mục tiêu: Cho hai danh sách, một chứa tên học sinh và một chứa điểm số tương ứng. Sử dụng zip() và enumerate() để in ra tên và điểm của từng học sinh, kèm theo thứ tự trong danh sách.
# Yêu cầu:
# Tạo hai danh sách: students (tên học sinh) và scores (điểm số).
# Sử dụng hàm zip() để kết hợp hai danh sách này lại.
# Sử dụng hàm enumerate() để lấy cả chỉ mục và cặp giá trị (tên, điểm) từ kết quả của zip().
# In ra kết quả theo định dạng mong muốn.

students = ["Stu", "dent", "test"]
score = [52,36,39]
combined = zip(students, score)

for thutu, (stu_name, stu_score) in enumerate(combined):
    print(f"{stu_name}'s score is {stu_score}")
#không dùng thutu

