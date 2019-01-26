
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

K, M = list(map(int,input().strip().split()))
X = []
for i in range(K):
    X.append(list(map(int,input().strip().split())))

X = [i[1:] for i in X]
cartesian_product = itertools.product(*X)
function_results = list(map(lambda z: sum(p**2 for p in z)%(M),cartesian_product))
print (max(function_results))