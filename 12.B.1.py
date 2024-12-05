def poisk_max():
    n = int(input("Введите число: "))
    if n == 0:
        return 0
    max_v_posled = poisk_max()
    return max(n, max_v_posled)


print("Наибольшее число в последовательности:", poisk_max())