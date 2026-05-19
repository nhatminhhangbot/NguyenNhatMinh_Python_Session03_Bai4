print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

# Sử dụng vòng lặp while để ép cấu trúc nhập liệu đúng điều kiện
while True:
    # Yêu cầu HR nhập số lượng nhân sự mới
    count = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))

    # Kiểm tra bẫy dữ liệu: Số lượng phải lớn hơn 0
    if count <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.")
    else:
        # Nếu dữ liệu hợp lệ, ghi nhận yêu cầu cấp phát tài sản và thoát vòng lặp
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {count} nhân sự mới!")
        break

print("--- CHƯƠNG TRÌNH KẾT THÚC ---")