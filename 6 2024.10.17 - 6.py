a = input().lower()
print(a)
b = ''
c = 0
s = 0
for i in a:
    s += 1
    if i != 'а':
        b += i
        c += 1
print(b, s - c)
