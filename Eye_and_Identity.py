import numpy as np
elements = raw_input().split()
int_elements = list(map(int,elements))
result = np.eye(int_elements[0],int_elements[1])
print result
