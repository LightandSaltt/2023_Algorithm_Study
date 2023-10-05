alp = [i for i in range(ord("a"), ord("z")+1)] # 알파벳 a ~ z 를 유니코드 정수변환으로 리스트 생성
str = list(input())
result = [-1]*26 # 결과 리스트에 미리 -1를 26개만큼 채워놓기
for i in range(0,len(str)):
  for j in range(0,26):
    if str[i] == chr(alp[j]): # i는 0 ~ str길이-1 / j는 0 ~ 25 반복 
      if result[j] == -1: # 중복값이 오면 먼저 온 순서를 등록하기 위해서 (덮어씌우지 않기 위함) 
        result[j] = i
for i in range(26):
  print(result[i], end = " ")