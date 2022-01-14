def dictionary(d):
    d = dict()
    for i in range(1, n + 1, 1):
        d[i] = i * i
    print(d)
name = input("Nhập Tên: ")
print("Tên đầy đủ vừa nhập:", name)
n = int(input("Nhập một số nguyên n: "))
print("Dictionary là:")
dictionary(n)