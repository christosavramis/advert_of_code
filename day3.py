#@title Day3
def day3():
  data = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/main/day3.txt').to_numpy().flatten()
  data = np.insert(data, 0, '110001101000')
  grate = ""
  erate = ""
  bits = np.zeros((12))
  counters = np.zeros((12))
  for dat in data:
    row = str(dat).zfill(12)
    for i in range(12):
      bits[i] += int(row[i])
  

  max_bit = data.shape[0]/2
  for i in range(12):
    if bits[i] > max_bit:
      grate+="1"
      erate+="0"
    else:
      grate+="0"
      erate+="1"
  # print(int(grate, 2)*int(erate, 2))
  print("life support rating of the submarine",day3ba() * day3bb())

def day3ba():
  data2 = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/main/day3.txt', header=None, dtype=str)[0].str.split('',expand=True).drop(columns=[0, 13])
  # data = ["00100" ,"11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
  # data2 = pd.DataFrame(data)[0].str.split('',expand=True).drop(columns=[0, 6])
  
  i=1
  while(True):
    select_bit = 0
    bit0 = data2.loc[(data2[i] == '0')].shape[0]
    bit1 = data2.loc[(data2[i] == '1')].shape[0]
    if bit0 <= bit1:
      select_bit = 1
    data2 = data2.loc[(data2[i] == str(select_bit))]
    if(data2.shape[0] == 1):
      break
    i+=1

  co2 = "".join(data2.to_numpy().flatten())
  # print(int(co2, 2))
  return int(co2, 2)

def day3bb():
  data2 = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/main/day3.txt', header=None, dtype=str)[0].str.split('',expand=True).drop(columns=[0, 13])
  # data = ["00100" ,"11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
  # data2 = pd.DataFrame(data)[0].str.split('',expand=True).drop(columns=[0, 6])
  
  i=1
  while(True):
    select_bit = 0
    bit0 = data2.loc[(data2[i] == '0')].shape[0]
    bit1 = data2.loc[(data2[i] == '1')].shape[0]
    if bit0 > bit1:
      select_bit = 1
    data2 = data2.loc[(data2[i] == str(select_bit))]
    if(data2.shape[0] == 1):
      break
    i+=1

  co2 = "".join(data2.to_numpy().flatten())
  print(int(co2, 2))
  return int(co2, 2)
  
day3()
