# Hãng hàng không X có chính sách giá vé như sau:  
# 1. **Giá vé gốc:** 2.000.000 VND  
# 2. **Giảm giá theo độ tuổi:**  
#    - Trẻ em (< 12 tuổi): giảm 50%  
#    - Người già (≥ 60 tuổi): giảm 30%  
#    - Các trường hợp khác: không giảm  
# 3. **Ưu đãi hội viên:**  
#    - Thành viên Gold: giảm thêm 20% *sau khi* áp dụng giảm giá theo độ tuổi  
#    - Thành viên Silver: giảm thêm 10% *sau khi* áp dụng giảm giá theo độ tuổi
#    - Không phải hội viên: không giảm thêm  
# 4. **Phụ phí hành lý:**  
#    - Nếu hành lý ký gửi > 20 kg → cộng thêm 50.000 VND cho mỗi kg vượt quá  

# **Yêu cầu:** Viết chương trình Python để:  
# - Nhập tuổi, loại hội viên (**Gold** hoặc **None**) và số kg hành lý ký gửi  
# - Tính **giá vé cuối cùng phải trả**  
# - In ra **mức giảm giá áp dụng** và **số tiền phải trả**  

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Input
tuoi_str = input("Nhập tuổi: ")
hoi_vien = input("Nhập loại hội viên: ").upper()
hanh_ly = input("Nhập số kg hành lý ký gửi: ")
gia_ve_goc = 2000000
gia_ve = 2000000
is_gold = 0
is_silver = 0
if hoi_vien == "GOLD": is_gold = 1
elif hoi_vien == "SILVER": is_silver = 1

# Áp dụng giảm giá vé theo độ tuổi
if tuoi_str.isdigit():
    tuoi = int(tuoi_str)
    if 0 < tuoi:
        if tuoi < 12:
            gia_ve *= 0.5
        elif tuoi >= 60:
            gia_ve *= 0.7
    else:
        print("Vui lòng nhập tuổi của người thực: ")
else:
    print("Dữ liệu đầu vào không hợp lệ.")

# Áp dụng giảm giá vé theo hạng thành viên
if is_gold == 1:
    gia_ve *= 0.8
elif is_silver == 1:
    gia_ve *= 0.9

# Tính phụ phí hành lý
if is_float(hanh_ly):
    hanh_ly = float(hanh_ly)
    phu_phi = (hanh_ly - 20) * 50000 if hanh_ly > 20 else 0
else:
    print("Dữ liệu hành lý không hợp lệ.")


muc_giam_gia = gia_ve_goc - gia_ve
tong_tien = gia_ve + phu_phi
print(f"Mức giảm giá áp dụng: {muc_giam_gia:,.0f} VND")
print(f"Số tiền phải trả (đã tính phụ phí hành lý): {tong_tien:,.0f} VND")
