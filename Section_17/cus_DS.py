# Bài Thực Hành 2: Phân Tích Dữ Liệu Khách Hàng (Tuple & Set)
# Mục tiêu
# Kết hợp sử dụng cả Tuple và Set để xử lý dữ liệu hiệu quả.
# Áp dụng các toán tử tập hợp (union, intersection) để giải quyết bài toán thực tế.
# Nội dung
# Bạn có dữ liệu về các giao dịch của khách hàng. Mỗi giao dịch được lưu dưới dạng một tuple chứa (mã_giao_dịch, mã_khách_hàng).
don_hang_thang_1 = [(101, "KH001"), (102, "KH002"), (103, "KH001"), (104, "KH003")]
don_hang_thang_2 = [(201, "KH002"), (202, "KH004"), (203, "KH005"), (204, "KH002")]
# Yêu cầu
# Sử dụng List Comprehension để tạo một danh sách mới chỉ chứa mã khách hàng từ don_hang_thang_1.
# Chuyển đổi danh sách mã khách hàng từ cả hai tháng thành các Set để loại bỏ các mã khách hàng trùng lặp.
# Tìm ra tổng số khách hàng duy nhất đã thực hiện giao dịch trong cả hai tháng.
# Tìm những khách hàng đã mua hàng trong cả hai tháng.

mkh_t1 = [don_hang_thang_1[i][1] for i in range(len(don_hang_thang_1))]
mkh_t2 = [don_hang_thang_2[i][1] for i in range(len(don_hang_thang_2))]
set_kh_t1 = set(mkh_t1)
set_kh_t2 = set(mkh_t2)
set_2t = set_kh_t1 | set_kh_t2
print(f"Tổng số khách hàng giao dịch ở cả 2 tháng là: {len(set_2t)}")
set_damua_2t = set_kh_t1 & set_kh_t2
print(f"Các khách hàng đã mua ở cả 2 tháng là {set_damua_2t}")
