# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = list(map(int,input().strip().split()))

wordsA = []
wordsB = []
for A in range(n):
    wordsA.append(input())
for B in range(m):
    wordsB.append(input())

inds = defaultdict(list)
for b in wordsB:
    if b in wordsA:
        inds[b].extend([str(k+1) for k,v in enumerate(wordsA) if v == b])
    else:
        inds[b].append(str(-1))
for key in inds:
    print (' '.join(inds[key]))
