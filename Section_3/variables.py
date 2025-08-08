from datetime import datetime

name = input("Your name: ")
birth_year = int(input("Your birth year: "))
height = float(input("Your height (in meters): "))
is_student = input("Are you a student (Y/N)?: ")
current_year = datetime.now().year

# Tính tuổi người dùng hiện tại
user_current_age = current_year - birth_year

# Kiểm tra xem người dùng có là học sinh không
if is_student == "Y":
    is_student = 1
else:
    is_student = 0

# Chương trình in kết quả ra màn hình
def output(user_name, user_current_age, user_height, user_is_student):
    print(
        f"Hello {user_name} \nYou are {user_current_age} years old \nYou are {user_height} meters tall"
    )
    if user_is_student == 1:
        print(f"You are a student")
    else:
        print(f"You are not a student")


output(name, user_current_age, height, is_student)

# Chương trình in số tuổi người dùng sau một năm
def after_one_year(user_current_age):
    user_current_age += 1
    print(f"After one year, you are {user_current_age} years old")


after_one_year(user_current_age)
