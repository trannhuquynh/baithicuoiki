def soThuanNghich(n):
    so_1 = str(n)
    so_2 = so_1[::-1]
    if (so_1 == so_2):
        print(n, "là số thuật nghịch!")
    else:
        print(n, "không phải là số thuật nghịch!")
ten = input("Nhập họ tên: ")
print("Họ tên đầy đủ là:", ten)
n = int(input("Nhập số nguyên dương n: "))
soThuanNghich(n)
