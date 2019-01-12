import numpy as np
N = int(raw_input())
arr_A = []
for i in range(N):
    inp = raw_input().split()
    user_inp = list(map(int,inp))
    arr_A.append(user_inp)
arr_B = []
for i in range(N):
    inp_ = raw_input().split()
    user_inp_ = list(map(int,inp_))
    arr_B.append(user_inp_)
    
print np.dot(arr_A,arr_B)
