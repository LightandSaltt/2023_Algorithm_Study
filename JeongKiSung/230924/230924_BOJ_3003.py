chess = [1,1,2,2,2,8]
a = list(map(int,input().split()))
for i in range(0,len(chess)):
  if a[i] == chess[i]:
    print(0, end = " ")
  else:
    print(chess[i] - a[i], end = " ")