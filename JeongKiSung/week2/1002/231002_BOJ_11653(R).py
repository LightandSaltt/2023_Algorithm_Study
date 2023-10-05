N = int(input())
count = 2
while count <= N:
  if N % count == 0:
    print(count)
    N = N / count
  else:
    count += 1