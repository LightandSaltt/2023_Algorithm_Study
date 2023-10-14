N, M = map(int, input().split())

L = []
for i in range(N):
    L.append(0)

# print(L)

for i in range(M):
    i, j, k = map(int, input().split())
    for n in range(i,j+1):
        L[n-1] = k

for i in range(N):
    print(L[i], end = ' ')