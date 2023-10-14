H, M = map(int, input().split())


H = H*60

a = H + M - 45


if a < 0:
    a += 24 * 60


H2 = a // 60

M2 = a % 60

print(H2, M2)
