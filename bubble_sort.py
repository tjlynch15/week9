import random

def sort(items):
  # 1. TO DO: Implement a "bubble sort" routine here
 
  in_order = False 

  while in_order == False:    
    in_order = True
    for j in range(len(numbers)-1):    
      if items[j] > items[j+1]:
        in_order = False
        items[j], items[j+1] = items[j+1], items[j]
       
  return(items)



numbers = list(range(10))
random.shuffle(numbers)

assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")

# 2. Change this print statement to display the complexity category.
#    Refer to the cheat sheet in week9-class for examples.
print("This algorithm is classified as: O(n^2)")
