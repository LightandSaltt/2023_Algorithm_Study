N = int(input()) # 분할 정복법

def moo(acc, cur, N): # acc = Moo(n)의 길이 / cur = 가운데 부분의 길이 
    prev = (acc-cur)//2
    if N <= prev: return moo(prev, cur-1, N)
    elif N > prev+cur: return moo(prev, cur-1, N-prev-cur)
    else: return "o" if N-prev-1 else "m"

acc, n = 3, 0
while N > acc:
    n += 1
    acc = acc*2+n+3

print(moo(acc, n+3, N))