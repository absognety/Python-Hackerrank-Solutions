# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

strg,k = input().strip().split()
strg = ''.join(sorted(strg))
perms = list(itertools.permutations(strg,int(k)))
for p in perms:
    print (''.join(p))