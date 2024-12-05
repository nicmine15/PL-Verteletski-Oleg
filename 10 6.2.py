file = open('Verteletski_O.S._У-243_vvod.txt.txt', 'r')
linii = file.readlines()

def swap_max_diagonal(m):
  n = len(m)
  d1 = [m[i][i] for i in range(n)]
  d2 = [m[i][n-i-1] for i in range(n)]
  max_val = max(max(d1), max(d2))
  i = d1.index(max_val) if max_val in d1 else d2.index(max_val)
  m[i][i], m[n//2][n//2] = m[n//2][n//2], m[i][i]
  return m

n = 5
m = []
for i in linii:
    cl = i.replace('[', '').replace(']', '').replace(',', '').strip()
    if cl:
        row = list(map(int, cl.split()))
        m.append(row)
m = swap_max_diagonal(m)

for i in range(n):
    print(m[i])

result = open('Verteletski_O.S._У-243_vivod_6.2.txt', 'w', encoding='utf-8')
result.write(f"m[i]")