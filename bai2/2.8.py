
#chuong trinh tim tong so chan trong day fibonacci
a, b = 1, 2
total = 0
print(a, end= " ")
while a <=4000000 - 1:
    if a % 2 == 0:
        total += a
    a, b = b, a+b
    print(a, end=" ")

print("tong cac so chan day Fibonacci:", total)
