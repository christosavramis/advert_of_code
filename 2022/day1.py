import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/main/2022/day1.txt', header=None, skip_blank_lines=False).fillna(0).to_numpy().flatten()
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