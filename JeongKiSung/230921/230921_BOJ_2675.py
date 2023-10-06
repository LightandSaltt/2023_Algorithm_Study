n = int(input())
for _ in range(n):
  R, S = map(str,input().split()) # R과 S 일단 string 형태로 받고
  R = int(R) # R만 int형으로 변환 - R은 반복횟수이기 때문
  for i in range(len(S)):
    print(S[i]*R, end = "") # 인덱스 i번째 R번 나오도록
  print() # == print(end = "\n")