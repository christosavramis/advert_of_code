def day2():
  data = pd.read_csv('https://raw.githubusercontent.com/christosavramis/advert_of_code/96f198b6177fc2c2651443907340ff134a43c703/day2').to_numpy().flatten()
  forward = 2
  depth = 0
  
  # data = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

  for dat in data:
   dir, val = dat.split(" ")
   if dir == "forward":
     forward += int(val)
   elif dir == "down":
     depth += int(val)
   else:
     depth -= int(val)
  print(forward*depth) 

  forward = 2
  depth = 0
  aim = 0
  for dat in data:
   dir, val = dat.split(" ")
   if dir == "forward":
     forward += int(val)
     depth += aim*int(val)
   elif dir == "down":
     aim += int(val)
   else:
     aim -= int(val)
  print(forward*depth) 
day2()
