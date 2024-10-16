n = int(input())
if n >= 2:
    for i in range(2, n + 1):
        if n % i == 0:
            print(i)
            break
elif n < 2:
    print('n < 2')