N = int(input())
num = list(map(int, input().split()))
for i in range(len(num)):
  factor = []
  for j in range(1,num[i]+1):
    if num[i] % j == 0:
      factor.append(j)
  if len(factor) != 2:
    N -= 1
print(N)