# Viết chương trình hiển thị số ngày trong tháng

month = int(input("Nhập tháng cần kiểm tra: "))
year = int(input("Nhập năm cần kiểm tra: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"Tháng {month} có 31 ngày.")
    case 4 | 6 | 9 | 11:
        print(f"Tháng {month} có 30 ngày.")
    case 2 if is_leap:
         print("Tháng 2 có 29 ngày (năm nhuận).")
    case 2:
        print("Tháng 2 có 28 ngày.")
    case _:
        print("Tháng không hợp lệ! Vui lòng nhập từ 1 đến 12.")
