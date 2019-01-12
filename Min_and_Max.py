import numpy as np
inp = raw_input().split()
N,M = list(map(int,inp))
arr = []
for i in range(N):
    user_inp = raw_input().split()
    user_int = list(map(int,user_inp))
    arr.append(user_int)
arr_trans = np.array(arr).reshape(N,M)
array = np.min(arr_trans,axis = 1)
result = max(array)
print result
