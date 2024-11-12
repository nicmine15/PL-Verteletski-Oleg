import math
def tri(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
def rect(a, b):
    s = a * b
    return s
def circ(r):
    s = math.pi * (r ** 2)
    return print(s)


n = int(input('Введите кол-во сторон (0 - круг):'))
if n == 3:
    a = int(input())
    b = int(input())
    c = int(input())
    print(tri(a, b, c))
elif n == 4:
    a = int(input())
    b = int(input())
    print(rect(a, b))
elif n == 0:
    r = int(input())
    print(circ(r))