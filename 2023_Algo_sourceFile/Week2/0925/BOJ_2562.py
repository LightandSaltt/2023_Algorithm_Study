numb_list = []

for i in range(9):
    numb_list.append(int(input()))
    
print(max(numb_list))
print(numb_list.index(max(numb_list))+1) # 0번부터 시작이니 +1