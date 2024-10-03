n = int(input())
a = 1   #a <=> n!
for i in range(1, n + 1):
    a *= i
print(a)