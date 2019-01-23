import itertools

strg,k = input().strip().split()
strg = ''.join(sorted(strg))
combs = []
for c in range(1,int(k)+1):
    combs.extend(list(itertools.combinations(strg,c)))
for combination in combs:
    print (''.join(combination))
