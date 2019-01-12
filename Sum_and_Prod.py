import numpy as np
elements = raw_input().split()
N,M = list(map(int,elements))
n = []
for i in range(N):
    N_ = raw_input().split()
    n_ = list(map(int,N_))
    n.append(n_)
sm = np.sum(n,axis = 0)
print np.prod(sm)