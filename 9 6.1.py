def maxstr_mincstol(m):
  n = len(m)
  maxstr = [max(r) for r in m]
  minstol = [min(m[i][j] for i in range(n)) for j in range(n)]
  return maxstr, minstol

m = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

maxstr, minstol = maxstr_mincstol(m)

print("максимальные элементы в строках:", maxstr)
print("минимальные элементы в столбцах:", minstol)