N, M = map(int, input().split())

l = []

for i in range(1, N+1):
    l.append(i)

for k in range(M):
    i, j = map(int, input().split())
    temp = l[i-1:j]
    temp.reverse()
    l[i-1:j] = temp
    # for z in range(i, j+1):
    #     l[z-1], l[j-1] = l[j-1], l[z-1]
    #     j -= 1
    #     if j == i:
    #         break


for i in l:
    print(i, end= ' ')
print()