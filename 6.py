a = int(input())
a1 = int(input())
b = int(input())
b1 = int(input())
if (a <= 8 and a1 <= 8 and b <= 8 and b1 <= 8) and (a > 0 and a1 > 0 and b > 0 and b1 > 0):
    if (a % 2 == 0 and a1 % 2 == 0 and b % 2 == 0 and b1 % 2 == 0) or \
        (a % 2 == 0 and a1 % 2 == 0 and b % 2 != 0 and b1 % 2 != 0) or \
        (a % 2 != 0 and a1 % 2 != 0 and b % 2 == 0 and b1 % 2 == 0) or \
        (a % 2 != 0 and a1 % 2 != 0 and b % 2 != 0 and b1 % 2 != 0) or \
        (a % 2 != 0 and a1 % 2 == 0 and b % 2 == 0 and b1 % 2 != 0) or \
        (a % 2 == 0 and a1 % 2 != 0 and b % 2 != 0 and b1 % 2 == 0) or \
        (a % 2 != 0 and a1 % 2 == 0 and b % 2 != 0 and b1 % 2 == 0) or \
        (a % 2 == 0 and a1 % 2 != 0 and b % 2 == 0 and b1 % 2 != 0):
        print("Да")
    else:
        print("Нет")
else:
    print('Цифры вне доски')
