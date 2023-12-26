n = int(input())
info_list = []

for i in range(n):
    age, name = input().split()
    info_list.append([int(age), name])
    
info_list.sort(key=lambda x:int(x[0]))

for i in info_list:
    print(i[0], i[1])