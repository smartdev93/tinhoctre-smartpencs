def dao_nguoc(x):
    # Đảo chữ số bằng phép chia lấy dư - cách làm giống trên Scratch
    r = 0
    while x > 0:
        r = r * 10 + x % 10
        x //= 10
    return r


def solve_so_doi_xung():
    n = int(input().strip())
    arr = list(map(int, input().split()))

    # Danh sách phụ: chỉ giữ các số đối xứng
    doi_xung = []
    for x in arr:
        if dao_nguoc(x) == x:
            doi_xung.append(x)

    # Sắp xếp chèn: đơn giản, dễ chuyển sang Scratch
    for i in range(1, len(doi_xung)):
        x = doi_xung[i]
        j = i - 1
        while j >= 0 and doi_xung[j] > x:
            doi_xung[j + 1] = doi_xung[j]
            j -= 1
        doi_xung[j + 1] = x

    tong_le = 0
    for x in doi_xung:
        if x % 2 == 1:
            tong_le += x

    if doi_xung:
        print(*doi_xung)
    else:
        print(-1)
    print(tong_le)


if __name__ == "__main__":
    solve_so_doi_xung()
