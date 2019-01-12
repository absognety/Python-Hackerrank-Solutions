N = int(input())
m = str(N)
for i in range(1,N,1):
    j = N-i
    m = str(j) + m
print(m)