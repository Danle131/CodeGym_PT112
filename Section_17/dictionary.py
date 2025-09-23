# Xây dựng ứng dụng từ điển
# Mục tiêu
# Hiểu cách sử dụng từ điển (dict) trong Python.
# Thực hành thêm, xóa, cập nhật và tìm kiếm từ trong từ điển.
# Áp dụng vòng lặp và điều kiện để xây dựng ứng dụng thực tế.
# Mô tả
# Bài tập này yêu cầu xây dựng một ứng dụng từ điển đơn giản cho phép người dùng:

# Thêm từ mới vào từ điển.
# Xóa từ khỏi từ điển.
# Cập nhật nghĩa của từ.
# Tra cứu nghĩa của từ.
# Hiển thị toàn bộ từ điển.
# Hướng dẫn
# Bước 1: Khởi tạo từ điển
# Sử dụng kiểu dữ liệu dict để lưu trữ các từ và nghĩa tương ứng.
# Cấu trúc dữ liệu: {"từ": "nghĩa"}.
# Bước 2: Xây dựng chức năng thêm từ mới
# Yêu cầu người dùng nhập từ và nghĩa tương ứng.
# Kiểm tra xem từ đã tồn tại trong từ điển hay chưa.
# Nếu chưa tồn tại, thêm từ vào từ điển.
# Bước 3: Xây dựng chức năng xóa từ
# Yêu cầu người dùng nhập từ cần xóa.
# Kiểm tra xem từ có trong từ điển hay không.
# Nếu có, xóa từ khỏi từ điển.
# Bước 4: Xây dựng chức năng cập nhật nghĩa của từ
# Yêu cầu người dùng nhập từ cần cập nhật.
# Kiểm tra xem từ có tồn tại hay không.
# Nếu có, cập nhật nghĩa mới cho từ.
# Bước 5: Xây dựng chức năng tra cứu từ
# Yêu cầu người dùng nhập từ muốn tra cứu.
# Nếu từ có trong từ điển, hiển thị nghĩa.
# Nếu không có, thông báo rằng từ chưa được thêm vào từ điển.
# Bước 6: Hiển thị toàn bộ từ điển
# Duyệt qua danh sách và in tất cả các từ cùng với nghĩa của chúng.

dictionary = {}

def add_word():
    word = input("Nhập từ cần thêm vào từ điển: ")
    defi_w = input("Nhập định nghĩa cho từ đã thêm: ")
    dictionary[word] = defi_w

def del_word():
    word_to_del = input("Nhập từ cần xóa: ")
    if word_to_del in dictionary:
        del dictionary[word_to_del]
        print(f'{word_to_del} đã được xóa')
    else:
        print(f"Không tồn tại {word_to_del} trong từ điển")

def up_def():
    word_to_up = input("Nhập từ cần sửa định nghĩa: ")
    if word_to_up in dictionary:
        newdef = input("Nhập định nghĩa mới: ")
        dictionary[word_to_up] = newdef
    else:
        print(f"Không tồn tại {word_to_up} trong từ điển")

def search_word():
    word_to_search = input("Nhập từ cần tìm kiếm: ")
    if word_to_search in dictionary:
        print(f'{word_to_search} có nghĩa là {dictionary[word_to_search]}')
    else:
        print(f"Không tồn tại {word_to_search} trong từ điển")

def show_dict():
    print(dictionary)

print("""Từ điển có các chức năng
      1. Chức năng thêm từ mới
      2. Chức năng xóa từ
      3. Chức năng cập nhật nghĩa của từ
      4. Chức năng tra cứu từ
      5. Chức năng hiển thị toàn bộ từ điển""")

while True:
    userin = int(input("Nhập chức năng cần sử dụng từ điển (nhập các số 1, 2, 3, 4, 5, 6[exit]): "))
    if userin == 1:
        add_word()
    elif userin == 2:
        del_word()
    elif userin == 3:
        up_def()
    elif userin == 4:
        search_word()
    elif userin == 5:
        show_dict()
    elif userin == 6:
        print("Bye!")
        break
    else:
        print("Từ điển không có chức năng bạn cần tìm:))))")
