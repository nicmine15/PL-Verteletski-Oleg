def ms(m):
  n = len(m)
  s = [sum(m[i]) for i in range(n)]
  c = [sum(m[i][j] for i in range(n)) for j in range(n)]
  d1 = sum(m[i][i] for i in range(n))
  d2 = sum(m[i][n - i - 1] for i in range(n))
  return all(s[0] == x for x in s) and all(c[0] == x for x in c) and d1 == d2 and d1 == c[0]

mtrx = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
if ms(mtrx):
  print("Матрица является магическим квадратом")
else:
  print("Матрица не является магическим квадратом")