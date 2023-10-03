n = int(input())
for i in range(1, n+1):
    if(i==1 or i==n):
        print(" " * (n-i) + "*" * (2*i-1)) # 첫번쨰, n과 같은 때에는 그 수와 같은 개수의 별 출력
    else:
        print(" " * (n-i) + "*" + " " * (2*(i-1)-1) + "*") # 나머지는 그 사이 비움