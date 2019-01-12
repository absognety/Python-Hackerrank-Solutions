import numpy as np
Coef = raw_input().split()
X = float(raw_input())
coef = list(map(float,Coef))
print np.polyval(coef,X)