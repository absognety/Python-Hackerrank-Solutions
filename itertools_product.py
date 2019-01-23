from itertools import product

A = list(map(int,input().strip().split()))
B = list(map(int,input().strip().split()))

ans = [str(i) for i in list(product(A,B))]
print (' '.join(ans))

