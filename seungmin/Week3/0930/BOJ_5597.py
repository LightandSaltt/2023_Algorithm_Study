# 1부터 30까지의 리스트를 생성 
num = [i for i in range(1, 31)]

# 입력받은 숫자를 리스트에서 제거
for _ in range(28):
    data = int(input())
    num.remove(data)
print(min(num))
print(max(num))

# 두 개의 배열을 만드는게 아닌 하나의 배열에서 입력 받은 값을 제거하는 식으로 접근!