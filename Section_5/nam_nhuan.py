# Viết chương trình kiểm tra năm nhuận
year = int(input("Nhập năm cần kiểm tra: "))
print(f"{year} là năm nhuận" if (((year%4 == 0) and (year%100!=0)) or (year%400 == 0)) else f"{year} không là năm nhuận") 
