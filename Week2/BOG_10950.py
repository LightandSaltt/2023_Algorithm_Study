n = int(input())

d = []
for i in range(n):
    a, b =map(int, input().split())
    d.append(a+b)

for i in range(n):
    print(d[i])