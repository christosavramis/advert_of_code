def day1():
  data = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/main/input_1.txt').to_numpy().flatten()
  counter = 1
  for i in range(1,data.shape[0]):
    if data[i] > data[i-1]:
      counter+=1
  print(counter)

def day1B():
  data = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/main/input_1.txt').to_numpy().flatten()
  counter = 1
  for i in range(data.shape[0]-3):
    if data[i] < data[i+3]:
     counter+=1
  print(counter)

day1()
day1B()
