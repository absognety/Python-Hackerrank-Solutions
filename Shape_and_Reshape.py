import numpy as np
arr = input().strip().split(' ')
my_array = np.array(list(map(int,arr)))
new_array = my_array.reshape(3,3)
print (new_array)