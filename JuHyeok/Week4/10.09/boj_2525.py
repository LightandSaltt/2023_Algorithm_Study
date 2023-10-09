h1, m1 = map(int, input().split())
t = int(input())

m2 = (m1 + t) % 60
h2 = (h1 + (m1 + t) // 60) % 24

print(h2, m2)
