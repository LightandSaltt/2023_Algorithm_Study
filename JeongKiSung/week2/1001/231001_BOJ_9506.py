while 1:
  factor = []
  sum = 0
  N = int(input())
  if N == -1:
    break
  else:
    for i in range(1,N):
      if N % i == 0:
        factor.append(i)
    for i in range(len(factor)):
      sum += factor[i]
    if N == sum:
      print(f"{N} = ",end = "")
      for i in range(len(factor)):
        if factor[i] == 1:
          print(factor[i], end = "")
        else:
          print(f" + {factor[i]}",end = "")
      print()
    else:
      print(f"{N} is NOT perfect.")