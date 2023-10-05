N, B = input().split()
B = int(B)
result = 0
for i in range(len(N)):
  if N[i].isnumeric():
      result += int(N[i]) * (B**(len(N)-1-i))
  else:
    result += (ord(N[i])-55) * (B**(len(N)-1-i))
print(result)