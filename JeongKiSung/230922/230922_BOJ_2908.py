a, b = input().split()
a_rev = [0]*3 # [0, 0, 0]
b_rev = [0]*3 # [0, 0, 0]
for i in range(2, -1, -1):
  a_rev[2-i] = a[i] # a[2]부터 ~ a[0] 순으로 넣기
  b_rev[2-i] = b[i]
a_rev = "".join(a_rev)
b_rev = "".join(b_rev)
if a_rev > b_rev:
  print(a_rev)
else:
  print(b_rev)