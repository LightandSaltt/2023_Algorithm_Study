x = [0] * 3
y = [0] * 3
x_result = 0
y_result = 0
for i in range(3):
  x[i], y[i] = map(int, input().split())
for i in range(3):
  if x.count(x[i]) == 1:
    x_result = x[i]
  if y.count(y[i]) == 1:
    y_result = y[i]
print(x_result, y_result)