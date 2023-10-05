str = []
for _ in range(5): # 5번 입력받고
  str.append(input()) # 배열안에 문자열(배열) 저장
for i in range(15): # 
  for j in range(5): # [j:0~4][i:0~15]
    if i >= len(str[j]): # 입력받은 문자 5개들의 각 길이보다 i 가 같거나 크면
      continue # 반복문 뛰어넘기
    else:
      print(str[j][i],end="") # 그 외는 출력

# 세로로 출력하기 때문에 출력순서는
# str[0][0~str[0~5]-1]
# str[1][0~str[0~5]-1] ...