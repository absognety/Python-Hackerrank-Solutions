import numpy as np
inp = raw_input().split()
inp_ = raw_input().split()
inp_A = list(map(int,inp))
inp_B = list(map(int,inp_))
print np.inner(inp_A,inp_B)
print np.outer(inp_A,inp_B)