# Bài 3: Hệ thống đăng nhập và phân quyền
# Viết chương trình mô phỏng hệ thống đăng nhập đơn giản, phân quyền truy cập cho người dùng.
# Yêu cầu:
# Hỏi người dùng nhập tên đăng nhập và mật khẩu.
# Kiểm tra:
# Nếu tên đăng nhập là "admin" và mật khẩu là "admin123", in ra "Đăng nhập thành công! Chào mừng quản trị viên.".
# Nếu tên đăng nhập là "user" và mật khẩu là "user456", in ra "Đăng nhập thành công! Chào mừng người dùng.".
# Nếu tên đăng nhập hoặc mật khẩu sai, in ra "Tên đăng nhập hoặc mật khẩu không chính xác.".
# Kết hợp các toán tử logic (and, or, not) và câu lệnh if-elif-else để giải quyết bài toán này.


while 1:
    user_name = input("Tên đang nhập: ")
    password = input("Mật khẩu: ")
    
    if user_name == "admin" and password == "admin123":
        print("Đăng nhập thành công! Chào mừng quản trị viên.")
        break
    elif user_name == "user" and password == "user456":
        print("Đăng nhập thành công! Chào mừng người dùng.")
        break
    else:
        print("Tên đăng nhập hoặc mật khẩu không chính xác.")
