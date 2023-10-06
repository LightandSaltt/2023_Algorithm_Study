from typing import Any, Sequence

def bin_search(a: Sequence, key: Any):
    """시퀀스 a에서 key와 일치하는 요소를 이진 검색"""
    pl = 0           # 검색 범위 맨 앞 요소의 인덱스
    pr = len(a) - 1  # 검색 범위 맨 끝 요소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 중앙 요소의 인덱스
        if a[pc] == key:
            print(1, end = ' ')
            return
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break
    print(0, end = ' ')
    return  

N = int(input())
l1 = (list(map(int, input().split())))


M = int(input())
l2 = (list(map(int, input().split())))


l1.sort()
for i in l2:
    bin_search(l1, i)



