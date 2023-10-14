l = list(range(1, 31))

for i in range(28):
    a = int(input())  
    if a in l:
        l.remove(a)

for i in l:
    print(i)
