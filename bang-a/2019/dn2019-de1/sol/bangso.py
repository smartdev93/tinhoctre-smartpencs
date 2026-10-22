def solve_bang_so():
    n = int(input().strip())  # số lượng các số
    so = []
    for i in range(n):
        so.append(int(input().strip()))  # nhập từng số vào danh sách Số

    dem_lon_hon_5 = 0
    lon_nhat = so[0]
    tong_le = 0
    dem_chan = 0
    for x in so:
        if x > 5:
            dem_lon_hon_5 = dem_lon_hon_5 + 1
        if x > lon_nhat:
            lon_nhat = x
        if x % 2 == 1:
            tong_le = tong_le + x
        else:
            dem_chan = dem_chan + 1

    # danh sách Kết quả
    ket_qua = [dem_lon_hon_5, lon_nhat, tong_le, dem_chan]
    for v in ket_qua:
        print(v)


if __name__ == "__main__":
    solve_bang_so()
