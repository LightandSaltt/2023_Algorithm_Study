line_max = []
table = []
N = 0 
M = 0
for _ in range(9):
  a = list(map(int, input().split()))
  table.append(a)
  line_max.append(max(a))
for i in range(9):
  for j in range(9):
    if table[i][j] == max(line_max):
      N = i+1
      M = j+1
print(max(line_max))
print(N, M)