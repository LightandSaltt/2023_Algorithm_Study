N, M = map(int, input().split())
A = []
B = []
for _ in range(0, N):
  A.append(list(map(int,input().split()))) # 리스트안에 리스트넣기
for _ in range(0, N):
  B.append(list(map(int,input().split())))
for i in range(0, N):
  for j in range(0, M):
    print(A[i][j] + B[i][j] ,end = " ")
  print()