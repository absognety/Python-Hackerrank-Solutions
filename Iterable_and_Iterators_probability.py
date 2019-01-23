import itertools

N = int(input())
letters = ''.join(input().strip().split())
k = int(input())

combos = list(itertools.combinations(letters,k))
sample_space = len(combos)

contains_a_sum = 0
for combination in combos:
    if 'a' in combination:
        contains_a_sum+=1

print ('%.3f'%(contains_a_sum/sample_space))
