n = int(input())

if n == 0:
    result = 0
elif n == 1:
    result = 1
else:
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    result = fib[n]

print(result)
