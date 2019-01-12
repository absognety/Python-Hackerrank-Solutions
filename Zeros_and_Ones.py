import numpy as np
elements = raw_input().split()
int_elements = list(map(int,elements))
List = tuple(int_elements)
zeroes = np.zeros(List,dtype = np.int)
print zeroes
Ones = np.ones(List,dtype = np.int)
print Ones