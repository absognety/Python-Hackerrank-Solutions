import numpy as np
inp = raw_input().split()
N,M = list(map(int,inp))
arr = []
for i in range(N):
    user_inp = raw_input().split()
    user_int = list(map(int,user_inp))
    arr.append(user_int)
array = np.array(arr).reshape(N,M)
print np.mean(array,axis = 1)
print np.var(array,axis = 0)
print np.std(array)