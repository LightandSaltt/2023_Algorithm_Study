N, M = map(int, input().split())

L = []

for i in range(N):
    L.append(i+1)

for i in range(M):
    i , j = map(int, input().split())
    L[i-1], L[j-1] = L[j-1], L[i-1]


for i in range(N):
    print(L[i], end = ' ')  
