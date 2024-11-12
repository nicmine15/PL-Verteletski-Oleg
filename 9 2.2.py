def smena(m):
    n = len(m)
    for i in range(n):
        m[0][i], m[-1][i] = m[-1][i], m[0][i]
    return m

n = int(input())
a = []
for i in range(n):
    b = []
    for i in range(n):
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
a = smena(a)

for i in range(n):
  print(a[i])