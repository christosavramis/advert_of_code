import pandas as pd
import numpy as np
def day6():
  fish = '5,1,2,1,5,3,1,1,1,1,1,2,5,4,1,1,1,1,2,1,2,1,1,1,1,1,2,1,5,1,1,1,3,1,1,1,3,1,1,3,1,1,4,3,1,1,4,1,1,1,1,2,1,1,1,5,1,1,5,1,1,1,4,4,2,5,1,1,5,1,1,2,2,1,2,1,1,5,3,1,2,1,1,3,1,4,3,3,1,1,3,1,5,1,1,3,1,1,4,4,1,1,1,5,1,1,1,4,4,1,3,1,4,1,1,4,5,1,1,1,4,3,1,4,1,1,4,4,3,5,1,2,2,1,2,2,1,1,1,2,1,1,1,4,1,1,3,1,1,2,1,4,1,1,1,1,1,1,1,1,2,2,1,1,5,5,1,1,1,5,1,1,1,1,5,1,3,2,1,1,5,2,3,1,2,2,2,5,1,1,3,1,1,1,5,1,4,1,1,1,3,2,1,3,3,1,3,1,1,1,1,1,1,1,2,3,1,5,1,4,1,3,5,1,1,1,2,2,1,1,1,1,5,4,1,1,3,1,2,4,2,1,1,3,5,1,1,1,3,1,1,1,5,1,1,1,1,1,3,1,1,1,4,1,1,1,1,2,2,1,1,1,1,5,3,1,2,3,4,1,1,5,1,2,4,2,1,1,1,2,1,1,1,1,1,1,1,4,1,5'
  fish = np.fromstring(fish, dtype=int, sep=',')
  days = 80 # make it 256 for free system crash :))

  for day in range(0, days):
    #decrease time
    fish[:] -=1

    #count fish to add
    add_fish = np.count_nonzero(fish == -1)

    #Change 0 to 6
    fish = np.where(fish == -1, 6, fish)

    #Add the new fish
    fish = np.append(fish,  np.full((add_fish), 8, dtype=int))
    
    # print(day,fish.shape[0])
  print("fish count", fish.shape[0])

def day6b(days=256):
 
  fish = '5,1,2,1,5,3,1,1,1,1,1,2,5,4,1,1,1,1,2,1,2,1,1,1,1,1,2,1,5,1,1,1,3,1,1,1,3,1,1,3,1,1,4,3,1,1,4,1,1,1,1,2,1,1,1,5,1,1,5,1,1,1,4,4,2,5,1,1,5,1,1,2,2,1,2,1,1,5,3,1,2,1,1,3,1,4,3,3,1,1,3,1,5,1,1,3,1,1,4,4,1,1,1,5,1,1,1,4,4,1,3,1,4,1,1,4,5,1,1,1,4,3,1,4,1,1,4,4,3,5,1,2,2,1,2,2,1,1,1,2,1,1,1,4,1,1,3,1,1,2,1,4,1,1,1,1,1,1,1,1,2,2,1,1,5,5,1,1,1,5,1,1,1,1,5,1,3,2,1,1,5,2,3,1,2,2,2,5,1,1,3,1,1,1,5,1,4,1,1,1,3,2,1,3,3,1,3,1,1,1,1,1,1,1,2,3,1,5,1,4,1,3,5,1,1,1,2,2,1,1,1,1,5,4,1,1,3,1,2,4,2,1,1,3,5,1,1,1,3,1,1,1,5,1,1,1,1,1,3,1,1,1,4,1,1,1,1,2,2,1,1,1,1,5,3,1,2,3,4,1,1,5,1,2,4,2,1,1,1,2,1,1,1,1,1,1,1,4,1,5'
  fish = np.fromstring(fish, dtype=int, sep=',')

  #Group together fish from the same time group
  _, counts = np.unique(fish, return_counts=True)
  fishes = np.append(np.zeros((1), dtype=int), np.append(counts, np.zeros((3), dtype=int)))


  for day in range(0, days):
    #Store new babies
    first = fishes[0]
    
    #Rotate the list == increase timer
    for i in range(1, 9):
      fishes[i-1] = fishes[i]
    fishes[6] += first

    #Add the new baby fish
    fishes[8] = first
  print(fishes.sum())
  
day6()
day6b()
