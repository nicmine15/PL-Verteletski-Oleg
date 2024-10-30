n = int(input())
a = []
h = 10000
g = 0
for i in range(n):
    s = int(input())
    a.append(s)
    if s < h:
        h = s
        g = i
print(min(a))
print(g)
