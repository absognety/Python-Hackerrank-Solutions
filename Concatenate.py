import numpy as np
elements = raw_input().split()
N = int(elements[0])
M = int(elements[1])
P = int(elements[2])
lt = []
for i in range(N):
    N_ = raw_input().split()
    n = list(map(int,N_))
    lt.append(n)
mt = []
for i in range(M):
    M_ = raw_input().split()
    m = list(map(int,M_))
    mt.append(m)

result = np.concatenate((lt,mt)).reshape(N+M,P)
print(result)
