def s(a):
    g = sum(a), sum(a) / len(a)
    return g


a = []
b = []
c = []
na = int(input('Введите число, не больше 15: '))
for i in range(na):
    d = int(input())
    a.append(d)
nb = int(input('Введите число, не больше 15: '))
for i in range(nb):
    d = int(input())
    b.append(d)
nc = int(input('Введите число, не больше 15: '))
for i in range(nc):
    d = int(input())
    c.append(d)
print(s(a), s(b), s(c))
