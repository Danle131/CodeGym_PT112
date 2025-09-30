# Bài Thực Hành 1: Quản lý Thông tin Cá nhân (Tuple)
# Mục tiêu
# Hiểu cách sử dụng Tuple để lưu trữ các bộ dữ liệu bất biến.
# Thực hành truy cập và xử lý dữ liệu trong Tuple.
# Nội dung
# Bạn được giao nhiệm vụ lưu trữ thông tin cá nhân của một vài người. Mỗi người có một hồ sơ bao gồm: (Tên, Ngày sinh, Số căn cước công dân). Vì các thông tin này không thay đổi, Tuple là lựa chọn hoàn hảo.
# Yêu cầu
# Tạo một Tuple chứa thông tin của ít nhất 3 người.
# In ra màn hình thông tin của người thứ hai trong danh sách.
# Truy cập và in ra ngày sinh của người đầu tiên.
# Thử thay đổi "ngày sinh" của người thứ ba. Quan sát lỗi xảy ra và giải thích tại sao.
# Vì tuple là một immutable object, thay đổi nội dung sẽ dẫn đến lỗi. Một immutable object được định nghĩa là object mà không thể thay đổi được nội dung, nếu cố gắng thay đổi, Python sẽ báo lỗi.

Thongtin = []
songuoi = int(input("Nhập số số người cần đưa thông tin: "))
for i in range(songuoi):
    temp = []
    ten = input(f"Nhập họ và tên của người {i + 1}: ")
    ngaysinh = input(f'Nhập ngày sinh của {ten} (dd/mm/yyyy): ')
    cccd = input(f'Nhập số căn cước công dân của {ten}: ')
    temp.append(ten)
    temp.append(ngaysinh)
    temp.append(cccd)
    Thongtin.append(temp)
    temp = [] 
fixed_thongtin = tuple(Thongtin)
if (len(fixed_thongtin) > 2): 
    print(f"Thông tin của {fixed_thongtin[1][0]} là:\n Ngày sinh: {fixed_thongtin[1][1]} \n CCCD: {fixed_thongtin[1][2]}")
    print(f"Ngày sinh của {fixed_thongtin[0][0]} là: {fixed_thongtin[0][1]}")
else: pass