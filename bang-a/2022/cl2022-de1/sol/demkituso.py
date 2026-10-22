def dem_ki_tu_so():
    s = input()

    # Duyệt từng ký tự, gặp chữ số '0'..'9' thì tăng biến đếm
    dem = 0
    for c in s:
        if c >= "0" and c <= "9":
            dem = dem + 1

    print(dem)


if __name__ == "__main__":
    dem_ki_tu_so()
