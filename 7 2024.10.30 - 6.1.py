a = []
s = 0
k = 0
c = 0
for i in range(10):
    a.append(int(input()))
    s += a[i]
for j in range(10):
    if a[j] < (s / 10):
        k += 1
    elif a[j] > (s / 10):
        c += 1
print('кол-вл min =', k)
print('кол-во max =', c)
print('max =', max(a))
