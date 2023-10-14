l = []

for i in range(9):
    l.append(int(input()))

for i in range(9):
    if max(l) == l[i]:
        print(max(l))
        print(i+1)