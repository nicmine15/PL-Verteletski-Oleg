a = []
s = 0
for i in range(10):
    a.append(int(input()))
    if a[i] > 5:
        s += a[i]
print(s)
