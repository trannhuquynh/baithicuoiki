import re
str = ', '

in4 = input("Nhập vào chuỗi tên và mã sinh viên: ")
giatri = str.join(in4)

l=giatri.split(",")
t=tuple(l)

print ("Danh sách là: ",l, end=" ")
print("")
print ("Tuple là: ",t, end=" ")