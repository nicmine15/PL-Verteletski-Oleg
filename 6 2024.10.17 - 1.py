a = input().lower().split()
print(a)
b = ''
c = 0
for i in a:
    if i[0] == 'е':
        c += 1
print(c)
