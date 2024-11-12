def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


k1 = int(input())
k2 = int(input())
print(nod(k1,k2))
print((k1 * k2) // nod(k1, k2))
