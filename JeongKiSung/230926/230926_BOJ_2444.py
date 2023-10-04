n = int(input())
for i in range(0,n):
  print(" "*((n-1)-i)+"*"+"*"*(i*2))
for j in range(n-2,-1,-1):
  print(" "*((n-1)-j)+"*"+"*"*(j*2))