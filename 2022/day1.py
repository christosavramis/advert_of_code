sum = 0
max = 0
for dat in data:
  if (dat == 0):
    if (max < sum):
      max = sum
    sum = 0
  else:
    sum = sum + dat
max