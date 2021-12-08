def checkboard(board, key='c', value_instances=5):
  sum_col = board[board== key].notnull().sum()
  any_col_5 = sum_col[sum_col == value_instances].sum() >= value_instances

  if any_col_5: 
    return True
 
  board = board.T
  sum_row = board[board== key].notnull().sum()
  any_row_5 = sum_row[sum_row == value_instances].sum() >= value_instances
  return any_row_5

def sum_of_unmarkerd(board, winning_number, key='c', ):
  board[board == key]=0
  board = pd.DataFrame(board, dtype=int)
  return board.sum().sum() * winning_number

def day4():
  steps = "15,62,2,39,49,25,65,28,84,59,75,24,20,76,60,55,17,7,93,69,32,23,44,81,8,67,41,56,43,89,95,97,61,77,64,37,29,10,79,26,51,48,5,86,71,58,78,90,57,82,45,70,11,14,13,50,68,94,99,22,47,12,1,74,18,46,4,6,88,54,83,96,63,66,35,27,36,72,42,98,0,52,40,91,33,21,34,85,3,38,31,92,9,87,19,73,30,16,53,80".split(',')
  data_url = "https://raw.githubusercontent.com/christosavramis/advert_of_code/main/day4.txt"
  boards_a = pd.read_csv(data_url, skiprows=1, header=None, delim_whitespace=True, dtype=str)
  boards = []

  #Split data to 5x5 tables
  for i in range(100):
    boards.append(pd.DataFrame(boards_a.iloc[5*i:5*(i+1)], dtype=str))
  
  #gain some performance by not checking for bingo before the 5th value
  per_c = 5

  board_index = -1
  winning_number = -1
  while(len(steps)>0 and board_index == -1):
    per_c -= 1
    step = steps.pop(0)
    # print("Number ",step)
    for i in range(len(boards)):
      boards[i] = boards[i].replace(step, 'c')

      if per_c <= 0 and checkboard(boards[i]):
        board_index = i
        winning_number = step
        break
  print("Table")
  print(boards[board_index])
  print("board_index:", board_index)
  print("winning number:", winning_number)
  print("Score part 1:",sum_of_unmarkerd(boards[board_index], int(winning_number)))


def day4b():
  steps = "15,62,2,39,49,25,65,28,84,59,75,24,20,76,60,55,17,7,93,69,32,23,44,81,8,67,41,56,43,89,95,97,61,77,64,37,29,10,79,26,51,48,5,86,71,58,78,90,57,82,45,70,11,14,13,50,68,94,99,22,47,12,1,74,18,46,4,6,88,54,83,96,63,66,35,27,36,72,42,98,0,52,40,91,33,21,34,85,3,38,31,92,9,87,19,73,30,16,53,80".split(',')
  data_url = "https://raw.githubusercontent.com/christosavramis/advert_of_code/main/day4.txt"
  boards_a = pd.read_csv(data_url, skiprows=1, header=None, delim_whitespace=True, dtype=str)
  boards = []

  #Split data to 5x5 tables
  for i in range(100):
    boards.append(pd.DataFrame(boards_a.iloc[5*i:5*(i+1)], dtype=str))
  
  #gain some performance by not checking for bingo before the 5th value
  per_c = 5

  winlist = []
  winlist_c = {}.fromkeys(range(100),0)
  while(len(steps)>0):
    per_c -= 1
    step = steps.pop(0)
    # print("Number ",step)
    for i in range(len(boards)):
      if winlist_c[i] == 1: continue
      boards[i] = boards[i].replace(step, 'c')
      if per_c <= 0 and checkboard(boards[i]):
          winlist_c[i] = 1
          winlist.append([boards[i], step])
print("Table")
print(winlist[-1])
print("Score part 2:",sum_of_unmarkerd(winlist[-1][0], int(winlist[-1][1])))

day4()
day4b()


# Table
# [     0   1  2   3   4
# 150  9   0  0   0   0
# 151  0  80  0  16   0
# 152  0   0  0  73   0
# 153  0   0  0   0  85
# 154  0   3  0   0   0, '21']
# Score part 2: 5586
# Table
#       0   1   2   3   4
# 245   c  56   c  57  40
# 246   c   c  26  30  90
# 247   c   c   c   c   c
# 248  96   c  79  99  85
# 249  13  10  86  51  53
# board_index: 49
# winning number: 41
# Score part 1: 35711
