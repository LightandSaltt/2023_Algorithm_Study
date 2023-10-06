n = int(input())
num = list(map(int, input().split()))
s = num[0] # 첫번째 인덱스를 최솟값으로 정함
b = num[0] # 첫번째 인덱스를 최댓값으로 정함

for i in range(n):
    if num[i] < s: # 요소가 작으면
        s = num[i] # s를 요소로 최솟값 설정
    elif num[i] > b: # 요소가 크면
        b = num[i] # s를 요소로 최댓값 설정
        
print(s, b, end = ' ')