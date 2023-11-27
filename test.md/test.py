import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))


for i in range(n):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t

for i in n:
    print(a[i])
