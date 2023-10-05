M = int(input())
N = int(input())
prime = []
sum = 0
for i in range(M, N+1):
  factor = []
  for j in range(1,i+1):
    if i % j == 0:
      factor.append(j)
  if len(factor) == 2:
    prime.append(i)
if prime == []:
  print(-1)
else:
  for i in range(len(prime)):
    sum += prime[i]
  print(sum)
  print(min(prime))