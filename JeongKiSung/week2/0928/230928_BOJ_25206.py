credit = [0]*20
grade = [0]*20
credit_sum = 0
subject_sum = 0
for i in range(20):
  subject, credit[i], grade[i] = input().split()
  if grade[i] != "P":
    credit_sum += float(credit[i])
for i in range(20):
  if grade[i] == "A+":
    subject_sum += float(credit[i]) * 4.5
  elif grade[i] == "A0":
    subject_sum += float(credit[i]) * 4.0
  elif grade[i] == "B+":
    subject_sum += float(credit[i]) * 3.5
  elif grade[i] == "B0":
    subject_sum += float(credit[i]) * 3.0
  elif grade[i] == "C+":
    subject_sum += float(credit[i]) * 2.5
  elif grade[i] == "C0":
    subject_sum += float(credit[i]) * 2.0
  elif grade[i] == "D+":
    subject_sum += float(credit[i]) * 1.5
  elif grade[i] == "D0":
    subject_sum += float(credit[i]) * 1.0
  elif grade[i] == "F":
    subject_sum += float(credit[i]) * 0.0
if subject_sum > 0:
  print(round(subject_sum / credit_sum,6))
else:
  print(subject_sum / credit_sum)