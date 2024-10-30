n = int(input())
a = []
s = 0
for i in range(n):
    h = int(input())
    a.append(h)
    s += h
print(a)
for j in range(len(a)):
    a[0] = s / len(a)
print(a)
