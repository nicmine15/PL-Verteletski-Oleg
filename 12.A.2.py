def ostat(a, b):
    if a < b:
        return a
    else:
        return ostat(a - b, b)

a = int(input('Введите натуральное число a:'))
b = int(input('Введите натуральное число b:'))

result = ostat(a, b)
print(f"Результат вычисления для a = {a} и b = {b}: {result}")