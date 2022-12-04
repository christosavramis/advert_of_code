import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/main/2022/day2.txt', header=None)

data2 = data.copy()
data.loc[data[0] == 'A Z'] = 3
data.loc[data[0] == 'A X'] = 1 + 3
data.loc[data[0] == 'A Y'] = 8 
data.loc[data[0] == 'B X'] = 1 
data.loc[data[0] == 'B Y'] = 2 + 3 
data.loc[data[0] == 'B Z'] = 9 
data.loc[data[0] == 'C Z'] = 3 + 3 
data.loc[data[0] == 'C Y'] = 2
data.loc[data[0] == 'C X'] = 7

data2.loc[data2[0] == 'A Z'] = 6 + 2
data2.loc[data2[0] == 'A X'] = 0 + 3
data2.loc[data2[0] == 'A Y'] = 3 + 1 
data2.loc[data2[0] == 'B X'] = 0 + 1
data2.loc[data2[0] == 'B Y'] = 3 + 2  
data2.loc[data2[0] == 'B Z'] = 6 + 3
data2.loc[data2[0] == 'C Z'] = 6 + 1
data2.loc[data2[0] == 'C Y'] = 3 + 3
data2.loc[data2[0] == 'C X'] = 0 + 2
print(data.sum(), "\n", data2.sum())