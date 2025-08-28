# Viết chương trình kiểm tra năm nhuận
def leap_check(year):
    return ((year%4 == 0) and (year%100!=0)) or (year%400 == 0)

year_str = input("Nhập năm cần kiểm tra: ")

if year_str.isdigit():
    year = int(year_str)
    print("Là năm nhuận") if leap_check(year) else print("Không là năm nhuận")
