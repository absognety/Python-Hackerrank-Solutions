import numpy as np
elements = raw_input().split()
int_elements = list(map(float,elements))
print np.floor(int_elements)
print np.ceil(int_elements)
print np.rint(int_elements)