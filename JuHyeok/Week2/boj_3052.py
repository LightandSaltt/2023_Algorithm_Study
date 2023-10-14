l = []

for i in range(10):
    l.append(int(input()) % 42)

len =len( set(l))
print(len)