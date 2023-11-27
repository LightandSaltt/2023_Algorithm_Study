N = int(input())

numbers = []
for _ in range(N):
    number = int(input())
    numbers.append(number)

# 오름차순 정렬
sorted_numbers = sorted(numbers)

# 정렬된 결과 출력
for num in sorted_numbers:
    print(num)
