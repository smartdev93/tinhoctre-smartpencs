def so_tu(thu):
    # Chủ nhật (0) nghỉ, thứ K (2..7) nhớ K từ
    if thu == 0:
        return 0
    return thu


def ngay_mai(thu):
    if thu == 0:
        return 2  # Chủ nhật -> Thứ Hai
    if thu == 7:
        return 0  # Thứ Bảy -> Chủ nhật
    return thu + 1


def solve_tu_vung():
    k = int(input().strip())
    n = int(input().strip())

    # Mỗi tuần trọn vẹn (7 ngày) nhớ được 2+3+4+5+6+7 = 27 từ
    tong = (n // 7) * 27

    # Các ngày lẻ còn lại (< 7 ngày), bắt đầu từ ngày mai
    thu = ngay_mai(k)
    for i in range(n % 7):
        tong += so_tu(thu)
        thu = ngay_mai(thu)

    print(tong)


if __name__ == "__main__":
    solve_tu_vung()
