N, B = map(int,input().split())
result = []
while N != 0:
  if 10 <= N%B <= 35:
    result.append(chr((N%B)+55))
    N = N//B
  else:
    result.append(str(N%B))
    N = N//B
result.reverse()
print("".join(result))