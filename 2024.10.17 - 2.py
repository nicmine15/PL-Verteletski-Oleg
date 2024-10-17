a = input().strip()
c = 0
for i in range(len(a)):
    if a[i] == ':':
        a = a.replace(':', '%')
        c += 1
print(a, c)