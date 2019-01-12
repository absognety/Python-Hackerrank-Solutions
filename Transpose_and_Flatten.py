import numpy as np
dim = input().strip().split(' ')
dim_ = list(map(int,dim))
_ent_ = []
for i in range(dim_[0]):
    ent = input().strip().split(' ')
    ent_ = list(map(int,ent))
    _ent_.append(ent_)
result = np.array(_ent_).reshape(dim_[0],dim_[1])
print (result.T)
print (result.flatten())