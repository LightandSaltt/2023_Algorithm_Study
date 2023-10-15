N = int(input())
card1 = list(map(int,input().split()))
M = int(input())
card2 = list(map(int,input().split()))
card1.sort()

def search(target):
  first = 0
  last = N-1
  while True:
    mid = (first+last) // 2
    if card1[mid] == target:
      print(1,end = " ")
      break
    elif card1[mid] > target:
      last = mid - 1
    else:
      first = mid + 1
    if first > last:
      print(0, end = " ")
      break
for i in range(M):
    search(card2[i])