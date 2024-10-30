n = int(input())
a = []
b = []
c = []
for i in range(n):
    a.append(int(input()))
for j in range(n):
    if a[j] > 0:
        b.append(a[j])
    else:
        c.append(a[j])
print(b, c)