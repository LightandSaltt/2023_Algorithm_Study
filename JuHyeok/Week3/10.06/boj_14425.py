N, M = map(int, input().split())
S = set()

for i in range(N):
    S.add(input())

count = 0
for i in range(M):
    s2 = input()
    if s2 in S:
        count += 1
print(count)