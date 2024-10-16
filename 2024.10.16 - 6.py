a = int(input())
b = 0
q = 1
while a != b:
    b = a
    a += int(input())
    q += 1
    if a == b:
        print(a / (q - 1))
