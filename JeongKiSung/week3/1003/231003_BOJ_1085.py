x, y, w, h = map(int,input().split())
# 조건 : x <= w-1 , y <= h-1 를 생각하기
# (0,0)과 가깝다면 x, y가 더 크고
# (w,h)와 가깝다면 w - x, h - y 가 더 크다고 가정
# 총 4가지의 경우를 들어서 조건을 나눌 수 있음
if x > w - x:
  if y > h - y:
    if w - x < h - y:
      print(w - x)
    else:
      print(h - y)
  else:
    if w - x < y:
      print(w - x)
    else:
      print(y)
else:
  if y > h - y:
    if x < h - y:
      print(x)
    else:
      print(h - y)
  else:  
    if x < y :
      print(x) 
    else:
      print(y)