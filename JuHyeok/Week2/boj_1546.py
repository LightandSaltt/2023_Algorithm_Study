M = int(input())

l = list(map(int, input().split()))

max = max(l)
result = []
for i,j in enumerate(l):
    l[i] = j / max*100

print(sum(l)/M)     