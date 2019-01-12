import numpy as np
N = int(raw_input())
arr = []
for i in range(N):
    inputs = raw_input().split()
    user_inp = list(map(float,inputs))
    arr.append(user_inp)
array = np.array(arr).reshape(N,N)
print np.linalg.det(array)