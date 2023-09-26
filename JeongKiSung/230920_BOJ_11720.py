num = int(input()) # 숫자의 갯수
sum = list(map(int, input())) # 모두 더할 숫자들 리스트
result = 0 # 모두 더한 결괏값 저장 변수
for i in range(num):
  result += sum[i] # sum[0] + sum[1] + ... +sum[num-1]
print(result)