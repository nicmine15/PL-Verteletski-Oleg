n = int(input())
a = []
s = 0
c = 0
for i in range(n):
    b = []
    for i in range(n):
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            s += a[i][j]
            c += 1
print(s, c)