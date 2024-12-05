file = open('Verteletski_O.S._У-243_vvod.txt.txt', 'r')
linii = file.readlines()

m = []
for i in linii:
    cl = i.replace('[', '').replace(']', '').replace(',', '').strip()
    if cl:
        row = list(map(int, cl.split()))
        m.append(row)
def maxstr_mincstol(m):
  n = len(m)
  maxstr = [max(r) for r in m]
  minstol = [min(m[i][j] for i in range(n)) for j in range(n)]
  return maxstr, minstol

maxstr, minstol = maxstr_mincstol(m)

print("максимальные элементы в строках:", maxstr)
print("минимальные элементы в столбцах:", minstol)

result = open('Verteletski_O.S._У-243_vivod_6.1.txt', 'w', encoding='utf-8')
result.write(f"максимальные элементы в строках: {maxstr}")
result.write(f"\nминимальные элементы в столбцах: {minstol}")