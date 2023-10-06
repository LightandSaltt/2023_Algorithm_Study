n = int(input())
for i in range(n, 0, -1): # n부터 0까지 -1씩 줄어들면서
    print(' ' * (n-i) + '*' * ((2*i)-1))
for j in range(2, n + 1): # 1을 출력할 필요가 없으므로 2부터
    print(' ' * (n-j) + '*' * ((2*j)-1))