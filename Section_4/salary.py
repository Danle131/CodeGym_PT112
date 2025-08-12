# Yêu cầu 1: 
# Nhập dữ liệu Lương cơ bản (float) 
# Số giờ làm thêm (int) Số ngày nghỉ không phép (int) 
# Hệ số thưởng hiệu suất (float, ví dụ 1.2 nghĩa là +20% lương, 0.9 nghĩa là giảm 10%) 
# Yêu cầu 2: 
# Quy tắc tính toán Tiền làm thêm = số giờ làm thêm × (lương cơ bản / 160) × 1.5 (giả sử 160 giờ/tháng là tiêu chuẩn, 1.5 là hệ số trả OT) 
# Tiền phạt nghỉ = số ngày nghỉ không phép × (lương cơ bản / 22) (22 ngày làm việc tiêu chuẩn) 
# Tổng lương trước thưởng/phạt = lương cơ bản + tiền làm thêm − tiền phạt. 
# Áp dụng thưởng hiệu suất: lương_sau_thuong = tổng_lương_trước × hệ_số_thưởng Nếu lương_sau_thuong > 30_000_000, công ty sẽ trừ thêm thuế thu nhập cá nhân = 10% trên phần vượt quá. (không dùng if else)
# In toàn bộ kết quả

luong_co_ban = float(input("Nhập lương cơ bản: "))
so_gio_lam_them = int(input("Nhập số giờ làm thêm: "))
so_ngay_nghi_khong_phep = int(input("Nhập số ngày nghỉ không phép: "))
he_so_thuong_hieu_suat = float(input("Nhập hệ số thưởng hiệu suất: "))

tien_lam_them = so_gio_lam_them * (luong_co_ban / 160) * 1.5
tien_phat_nghi = so_ngay_nghi_khong_phep * (luong_co_ban / 22)

tong_luong_truoc = luong_co_ban + tien_lam_them - tien_phat_nghi
luong_sau_thuong = tong_luong_truoc * he_so_thuong_hieu_suat

tien_luong = luong_sau_thuong - (luong_sau_thuong > 30_000_000) * (luong_sau_thuong - 30_000_000) * 0.1

print(f"Tổng lương: {tien_luong:,.2f} VND")
