str = input()
num = [0 for i in range(0, len(str))]
result = 0
for i in range(0, len(str)):
  if str[i] == "A" or str[i] == "B" or str[i] == "C":
    num[i] = 3
  elif str[i] == "D" or str[i] == "E" or str[i] == "F":
    num[i] = 4
  elif str[i] == "G" or str[i] == "H" or str[i] == "I":
    num[i] = 5
  elif str[i] == "J" or str[i] == "K" or str[i] =="L":
    num[i] = 6
  elif str[i] == "M" or str[i] == "N" or str[i] == "O":
    num[i] = 7
  elif str[i] == "P" or str[i] =="Q" or str[i] == "R" or str[i] == "S":
    num[i] = 8
  elif str[i] == "T" or str[i] == "U" or str[i] == "V":
    num[i] = 9
  elif str[i] == "W" or str[i] == "X" or str[i] == "Y" or str[i] == "Z":
    num[i] = 10
for i in range(0, len(str)):
  result += num[i]
print(result)