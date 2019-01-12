import numpy as np
elements = raw_input().split()
int_elements = list(map(int,elements))
n_A = []
for i in range(int_elements[0]):
    N_ = raw_input().split()
    n = list(map(int,N_))
    n_A.append(n)
m_B = []
for i in range(int_elements[0]):
    M_ = raw_input().split()
    m = list(map(int,M_))
    m_B.append(m)
a = np.array(n_A)
b = np.array(m_B)

print np.add(a,b)
print np.subtract(a,b)
print np.multiply(a,b)
print np.divide(a,b)
print np.mod(a,b)
print np.power(a,b)
  