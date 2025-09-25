# Nhận một danh sách các phần tử từ người dùng.
# Đếm số lần xuất hiện của từng phần tử trong danh sách.
# Xác định phần tử xuất hiện nhiều nhất.
# Hiển thị kết quả ra màn hình.
# Input có dạng là một string chứa các phần tử cách nhau bởi dấu phẩy
# Output có dạng là một string là từ xuất hiện nhiều nhất
def do():
    usin = input("Nhập chuỗi cần check: ")
    w_usin = usin.split(",")
    tu = {}
    for i in w_usin:
        if i in tu:
            tu[i] += 1
        else:
            tu[i] = 1
    MAX = max(tu.values())
    sort_tu = sorted(tu.keys())
    for x in sort_tu:
        if tu[x] == MAX:
            print(x)
            break
    

do()
