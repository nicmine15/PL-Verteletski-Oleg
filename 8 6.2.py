import math
def fourangle(a, b, c, d, e):
    p1 = (a + b + c) / 2
    p2 = (c + d + e) / 2
    s1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - c))
    s2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - e))
    return s1 + s2


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
print(fourangle(a, b, c, d, e))