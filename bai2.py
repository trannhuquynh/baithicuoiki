def timtong(n):
    sum = 0
    tong = n
    while (n > 0):
        sum = sum + n % 10
        n = int(n / 10)
    print("Tổng các chữ số của", tong, "là:", sum)
tendem = input("Nhập tên đệm: ")
print("Tên đệm vừa nhập:", tendem)
n = int(input("Nhập số nguyên dương n = "))
timtong(n)

