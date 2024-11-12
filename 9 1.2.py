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
    max_element = max(a[i])
    min_element = min(a[i])
    max_index = a[i].index(max_element)
    min_index = a[i].index(min_element)
    a[i][max_index] = a[i][0]
    a[i][min_index] = a[i][-1]
    a[i][0] = max_element
    a[i][-1] = min_element
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()