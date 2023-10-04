str = input() 
count = 0
for i in range(len(str)):
  if i < len(str)-1: 
    if str[i]+str[i+1] == "c=":
      count += 1
    elif str[i]+str[i+1] == "c-":
      count += 1
    elif str[i]+str[i+1] == "d-":
      count += 1
    elif str[i]+str[i+1] == "lj":
      count += 1
    elif str[i]+str[i+1] == "nj":
      count += 1
    elif str[i]+str[i+1] == "s=":
      count += 1
    elif str[i]+str[i+1] == "z=":
      count += 1
    elif i < len(str)-2:
      if str[i]+str[i+1]+str[i+2] == "dz=":
        count += 1
print(len(str)-count)