import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/main/2022/day1.txt', header=None, skip_blank_lines=False).fillna(0).to_numpy().flatten()
sums = []
sumC = 0
for dat in data:
  if (dat == 0):
    sums.append(sumC)
    sumC = 0
  else:
    sumC = sumC + dat
sums = sorted(sums, reverse=True)
print("A ",  sums[0], "B ", sum(sums[:3]))